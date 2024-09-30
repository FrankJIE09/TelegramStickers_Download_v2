import os
import torch
from PIL import Image
from torchvision import transforms

# 文件夹路径
folder_path = './'

# 定义一个函数来将 PIL 图像转换为 PyTorch 张量
def pil_to_tensor(pil_image):
    transform = transforms.ToTensor()
    return transform(pil_image).unsqueeze(0)  # 添加 batch 维度

# 定义一个函数来将 PyTorch 张量转换回 PIL 图像
def tensor_to_pil(tensor_image):
    transform = transforms.ToPILImage()
    return transform(tensor_image.squeeze(0))  # 移除 batch 维度

def compress_gif(input_path, output_path, max_size, target_file_size, device):
    # 打开GIF文件
    with Image.open(input_path) as im:
        # 获取原始文件大小
        original_size = os.path.getsize(input_path)

        if original_size > target_file_size:
            current_scale_factor = 2  # 初始压缩比例
            while True:
                # 获取所有帧
                frames = []
                im.seek(0)  # 重置到第一帧
                try:
                    # 遍历GIF的所有帧
                    while True:
                        # 获取当前帧并缩小分辨率
                        frame = im.copy()

                        # 将 PIL 图像转换为 PyTorch 张量
                        frame_tensor = pil_to_tensor(frame).to(device)

                        # 使用 GPU 进行缩放操作，逐步减少分辨率
                        new_height = frame.height // current_scale_factor
                        new_width = frame.width // current_scale_factor
                        frame_resized = torch.nn.functional.interpolate(frame_tensor, size=(new_height, new_width), mode='bilinear')

                        # 将缩放后的张量转换回 PIL 图像
                        frame = tensor_to_pil(frame_resized.cpu())
                        frames.append(frame)
                        im.seek(im.tell() + 1)
                except EOFError:
                    pass  # 处理完所有帧

                # 将所有帧保存为压缩后的GIF
                frames[0].save(output_path, save_all=True, append_images=frames[1:], optimize=True, loop=0)

                # 再次检查压缩后文件大小
                compressed_size = os.path.getsize(output_path)

                if compressed_size <= target_file_size:
                    print(f"文件 {input_path} 已压缩至目标大小：{compressed_size} 字节")
                    break
                else:
                    print(f"文件 {input_path} 仍然大于目标大小，当前大小：{compressed_size} 字节，继续压缩")
                    # 增加压缩比例
                    current_scale_factor += 1
        else:
            print(f"文件 {input_path} 大小已符合要求，无需压缩")

# 选择使用的设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 遍历文件夹中的所有GIF文件
max_size = 1 * 1024 * 1024  # 设置为 1MB
for filename in os.listdir(folder_path):
    if filename.endswith('.gif'):
        input_gif = os.path.join(folder_path, filename)
        output_gif = os.path.join(folder_path, f"compressed_{filename}")
        compress_gif(input_gif, output_gif, max_size, max_size, device)
