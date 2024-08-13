import os
import asyncio
from telegram import Bot
from tqdm import tqdm
import requests

async def download_stickers(bot_token, sticker_set_name, output_folder):
    """从 Telegram 下载贴纸包"""
    try:
        # 设置超时时间并创建 Bot 对象
        bot = Bot(token=bot_token)
    except Exception as e:
        print(f"Failed to create bot: {e}")
        return

    try:
        sticker_set = await bot.get_sticker_set(name=sticker_set_name)
    except Exception as e:
        print(f"Failed to get sticker set '{sticker_set_name}': {e}")
        return

    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
    except Exception as e:
        print(f"Failed to create output directory '{output_folder}': {e}")
        return

    for sticker in tqdm(sticker_set.stickers, desc="Downloading Stickers"):
        file_id = sticker.file_id
        try:
            file = await bot.get_file(file_id)
            file_path = os.path.join(output_folder, f'{sticker.file_unique_id}.webp')

            try:
                # 下载文件
                file_url = file.file_path
                response = requests.get(file_url)
                response.raise_for_status()  # 检查请求是否成功

                # 将文件保存到本地
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            except requests.RequestException as e:
                print(f"Failed to download the file for sticker {file_id}: {e}")
                continue

        except Exception as e:
            print(f"Failed to process sticker {file_id}: {e}")
            continue

    print(f"Stickers from '{sticker_set_name}' have been downloaded and saved to {output_folder}.")

if __name__ == "__main__":
    bot_token = '5640863500:AAGgnofomUMC1zn9c8CmW5CnfJQhBtX7LUk'  # 替换为实际的 bot token
    sticker_set_name = 'biao2_by_TgEmojiBot'  # 替换为实际的 sticker 名称
    output_folder = f'{sticker_set_name}'
    asyncio.run(download_stickers(bot_token, sticker_set_name, output_folder))
