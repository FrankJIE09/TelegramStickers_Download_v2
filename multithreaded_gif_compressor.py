import os
import torch
import shutil  # 用于复制文件
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
from torchvision import transforms


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
            current_scale_factor = 1.2  # 初始压缩比例
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
                        new_height = int(frame.height / current_scale_factor)  # 将结果转换为整数
                        new_width = int(frame.width / current_scale_factor)  # 将结果转换为整数
                        frame_resized = torch.nn.functional.interpolate(
                            frame_tensor, size=(new_height, new_width), mode='bilinear'
                        )

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
            # 如果文件大小已符合要求，直接复制到输出目录
            shutil.copy(input_path, output_path)


# 选择使用的设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("device = ", device)

# 定义一个处理单个文件的函数，用于多线程调用
def process_file(input_gif, output_gif_folder, max_size, target_file_size, device, skip_existing=True):
    # 创建输出目录（如果不存在）
    os.makedirs(output_gif_folder, exist_ok=True)

    # 构建输出文件路径
    output_gif = os.path.join(output_gif_folder, os.path.basename(input_gif))

    # 如果设置了跳过已存在文件，并且目标文件已存在，则跳过
    if skip_existing and os.path.exists(output_gif):
        print(f"文件 {output_gif} 已存在，跳过处理")
        return  # 直接跳过该文件

    # 判断文件大小，压缩或复制
    if os.path.getsize(input_gif) <= target_file_size:
        # 如果文件大小符合要求，直接复制
        print(f"文件 {input_gif} 大小符合要求，直接复制到 {output_gif}")
        shutil.copy(input_gif, output_gif)
    else:
        # 如果文件需要压缩，调用压缩函数
        compress_gif(input_gif, output_gif, max_size, target_file_size, device)


# 遍历文件夹中的所有一级子文件夹中的GIF文件，使用多线程进行处理
max_size = 2 * 1024 * 1024  # 设置为 2MB
target_file_size = max_size

# 遍历一级子文件夹
input_folder = './'  # 输入的根目录
output_folder = './output_gif'  # 输出的根目录

# 设置是否跳过已存在的文件
skip_existing = True  # 可以更改为 False 以强制处理所有文件

# 获取一级子文件夹
for subdir in next(os.walk(input_folder))[1]:
    subdir_path = os.path.join(input_folder, subdir)
    output_subdir_path = os.path.join(output_folder, subdir)

    # 获取该子文件夹下的所有GIF文件
    gif_files = [f for f in os.listdir(subdir_path) if f.endswith('.gif')]

    # 使用 ThreadPoolExecutor 进行多线程处理
    with ThreadPoolExecutor(max_workers=10) as executor:
        # 提交任务到线程池
        futures = [
            executor.submit(
                process_file,
                os.path.join(subdir_path, gif_file),  # 输入GIF路径
                output_subdir_path,  # 输出的对应子文件夹路径
                max_size,
                target_file_size,
                device,
                skip_existing  # 传递跳过已存在文件的参数
            )
            for gif_file in gif_files
        ]

        # 等待所有线程执行完毕
        for future in futures:
            future.result()

print("所有 GIF 文件已处理完成。")
