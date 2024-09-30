import os
import shutil

def zip_gif_folders(base_folder):
    """将所有以 _gifs 结尾的文件夹打包为 zip 文件"""
    for folder_name in os.listdir(base_folder):
        if folder_name.endswith('_gifs'):
            folder_path = os.path.join(base_folder, folder_name)
            zip_path = os.path.join(base_folder, folder_name)  # 不加 .zip 后缀

            # 创建 zip 文件
            shutil.make_archive(zip_path, 'zip', folder_path)
            print(f"Folder '{folder_name}' has been zipped as '{folder_name}.zip'.")

if __name__ == "__main__":
    base_folder = '.'  # 设置为你的根文件夹路径
    zip_gif_folders(base_folder)
