import os
import imageio
from tqdm import tqdm
import subprocess


def convert_webp_to_gif(input_path, output_path):
    """将单个 .webp 文件转换为 .gif 文件，并动态调整帧率和持续时间"""
    try:
        images = imageio.mimread(input_path, memtest=False)
    except Exception as e:
        try:
            # 使用 ffmpeg 进行转换
            subprocess.run(['ffmpeg', '-i', input_path, output_path], check=True)
            print(f"Converted {input_path} to {output_path} using ffmpeg.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to convert {input_path} to {output_path} using ffmpeg: {e}")
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
    urls_file = 'url.txt'
    with open(urls_file, 'r') as file:
        urls = file.readlines()

    for url in urls:
        sticker_set_name = url.strip().split('/')[-1]
        input_folder = sticker_set_name
        output_folder = f"{sticker_set_name}_gifs"

        # 检查是否已经存在该文件夹，如果存在则跳过
        if os.path.exists(output_folder):
            print(f"Folder '{output_folder}' already exists. Skipping {sticker_set_name}.")
            continue

        convert_folder_webps_to_gifs(input_folder, output_folder)
