import os
def remove_empty_folders(path):
    # 先处理子文件夹
    for root, dirs, files in os.walk(path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            # 如果文件夹是空的，则删除
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Removed empty folder: {dir_path}")

# 指定当前文件夹
folder_path = "./"

remove_empty_folders(folder_path)
