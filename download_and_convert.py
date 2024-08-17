import os
import asyncio
import requests
from telegram import Bot
from tqdm import tqdm
import imageio
from convert_webp_to_gif import convert_webp_to_gif
from download_sticker import download_stickers

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


async def process_sticker_sets(bot_token, urls_file):
    with open(urls_file, 'r') as file:
        urls = file.readlines()

    for url in urls:
        sticker_set_name = url.strip().split('/')[-1]
        output_folder = sticker_set_name
        gif_output_folder = f"{sticker_set_name}_gifs"

        # 检查是否已经存在该文件夹，如果存在则跳过
        if os.path.exists(output_folder):
            print(f"Folder '{output_folder}' already exists. Skipping {sticker_set_name}.")
            continue

        # 下载贴纸包
        await download_stickers(bot_token, sticker_set_name, output_folder)

        # 将下载的贴纸包转换为 GIF
        convert_folder_webps_to_gifs(output_folder, gif_output_folder)


if __name__ == "__main__":
    # 7046331816: AAF0Rm_gdn5IKo842Z2fF12YFewqpZ6EsXg
    # 5640863500:AAGgnofomUMC1zn9c8CmW5CnfJQhBtX7LUk
    bot_token = '7046331816: AAF0Rm_gdn5IKo842Z2fF12YFewqpZ6EsXg'  # 替换为实际的 bot token
    urls_file = 'url.txt'
    asyncio.run(process_sticker_sets(bot_token, urls_file))
