import os
import asyncio
import requests
from telegram import Bot
from tqdm import tqdm
import imageio


async def download_stickers(bot_token, sticker_set_name, output_folder):
    """从 Telegram 下载贴纸包"""
    try:
        bot = Bot(token=bot_token)
    except Exception as e:
        print(f"Failed to create bot: {e}")
        return

    try:
        sticker_set = await bot.get_sticker_set(name=sticker_set_name)
    except Exception as e:
        print(f"Failed to get sticker set '{sticker_set_name}': {e}")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for sticker in tqdm(sticker_set.stickers, desc="Downloading Stickers"):
        file_id = sticker.file_id
        try:
            file = await bot.get_file(file_id)
            file_path = os.path.join(output_folder, f'{sticker.file_unique_id}.webp')

            try:
                file_url = file.file_path
                response = requests.get(file_url)
                response.raise_for_status()  # 检查请求是否成功

                with open(file_path, 'wb') as f:
                    f.write(response.content)
            except requests.RequestException as e:
                print(f"Failed to download the file for sticker {file_id}: {e}")
                continue

        except Exception as e:
            print(f"Failed to process sticker {file_id}: {e}")
            continue

    print(f"Stickers from '{sticker_set_name}' have been downloaded and saved to {output_folder}.")


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
        frame_duration = 1 / (len(reduced_images) / (len(images) / 30))
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
    bot_token = '5640863500:AAGgnofomUMC1zn9c8CmW5CnfJQhBtX7LUk'  # 替换为实际的 bot token
    urls_file = 'url.txt'
    asyncio.run(process_sticker_sets(bot_token, urls_file))
