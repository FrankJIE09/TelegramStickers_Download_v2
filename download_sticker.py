
import os
import asyncio
from telegram import Bot
from tqdm import tqdm
import requests
async def download_stickers(bot_token, sticker_set_name, output_folder):
    """从 Telegram 下载贴纸包"""
    bot = Bot(token=bot_token)
    sticker_set = await bot.get_sticker_set(name=sticker_set_name)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 创建一个文件夹来保存Sticker
    if not os.path.exists(sticker_set_name):
        os.makedirs(sticker_set_name)

    for sticker in tqdm(sticker_set.stickers, desc="Downloading Stickers"):
        file_id = sticker.file_id
        file = await bot.get_file(file_id)
        file_path = os.path.join(sticker_set_name, f'{sticker.file_unique_id}.webp')

        # 下载文件
        file_url = file.file_path
        response = requests.get(file_url)

        # 将文件保存到本地
        with open(file_path, 'wb') as f:
            f.write(response.content)

    print(f"Stickers from '{sticker_set_name}' have been downloaded and saved to {output_folder}.")

if __name__ == "__main__":
    bot_token = '5640863500:AAGgnofomUMC1zn9c8CmW5CnfJQhBtX7LUk'  # 替换为实际的 bot token
    sticker_set_name = 'niubiuniu_by_WuMingv2Bot'  # 替换为实际的 sticker 名称
    output_folder = f'{sticker_set_name}'
    asyncio.run(download_stickers(bot_token, sticker_set_name, output_folder))

