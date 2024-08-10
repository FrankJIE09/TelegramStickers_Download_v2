import asyncio
from download_sticker import download_stickers
from convert_webp_to_gif import convert_folder_webps_to_gifs

def main(sticker_name, bot_token):
    # 下载贴纸
    output_folder = f'{sticker_name}'
    asyncio.run(download_stickers(bot_token, sticker_name, output_folder))

    # 转换为 GIF
    gif_output_folder = f'{sticker_name}_gifs'
    convert_folder_webps_to_gifs(output_folder, gif_output_folder)

if __name__ == "__main__":
    # 提前写入 sticker_name 和 bot_token
    sticker_name = 'niubiuniu_by_WuMingv2Bot'  # 例如
    bot_token = '5640863500:AAGgnofomUMC1zn9c8CmW5CnfJQhBtX7LUk'
    main(sticker_name, bot_token)
