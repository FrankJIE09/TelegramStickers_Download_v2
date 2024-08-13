import os
import imageio
from tqdm import tqdm

def convert_webp_to_gif(input_path, output_path):
    """将单个 .webp 文件转换为 .gif 文件，并动态调整帧率和持续时间"""
    try:
        images = imageio.mimread(input_path, memtest=False)
    except Exception as e:
        print(f"Failed to read {input_path}: {e}")
        return

    try:
        reduction_factor = 3
        reduced_images = images[::reduction_factor]

        # 动态调整 duration，确保总时长为 total_duration
        frame_duration = 1 / (len(reduced_images) / (len(images) / 30))

        # 保存为 .gif 文件
        imageio.mimsave(output_path, reduced_images, format='GIF', duration=frame_duration)
    except Exception as e:
        print(f"Failed to convert {input_path} to GIF: {e}")
        return

def convert_folder_webps_to_gifs(input_folder, output_folder):
    """将文件夹中的所有 .webp 文件转换为 .gif，并保存到新的文件夹中"""
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
    except Exception as e:
        print(f"Failed to create output directory '{output_folder}': {e}")
        return

    webp_files = [f for f in os.listdir(input_folder) if f.endswith('.webp')]

    for filename in tqdm(webp_files, desc="Converting WEBP to GIF"):
        input_path = os.path.join(input_folder, filename)
        output_filename = filename.replace('.webp', '.gif')
        output_path = os.path.join(output_folder, output_filename)
        try:
            convert_webp_to_gif(input_path, output_path)
        except Exception as e:
            print(f"Failed to process {input_path}: {e}")
            continue

    print(f"All .webp files have been converted and saved to {output_folder}.")

if __name__ == "__main__":

    sticker_name = 'biaoqing82'  # 替换为实际的 sticker 名称
    input_folder = f'{sticker_name}'
    output_folder = f'{sticker_name}_gifs'
    convert_folder_webps_to_gifs(input_folder, output_folder)
