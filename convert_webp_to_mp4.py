import os
import imageio
import moviepy.editor as mp

def convert_webp_to_mp4(input_path, output_path, duration=2):
    """将 .webp 文件转换为 .mp4"""
    images = imageio.mimread(input_path)  # 读取 .webp 动图的每一帧
    clips = [mp.ImageClip(img).set_duration(duration / len(images)) for img in images]  # 创建每一帧的片段
    video = mp.concatenate_videoclips(clips, method="compose")  # 合并所有帧为一个视频
    video.write_videofile(output_path, codec='libx264', fps=24)  # 保存为 mp4 文件

def convert_folder_webps_to_mp4s(input_folder, output_folder, duration=2):
    """将文件夹中的所有 .webp 文件转换为 .mp4，并保存到新的文件夹中"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.webp'):
            input_path = os.path.join(input_folder, filename)
            output_filename = filename.replace('.webp', '_mp4.mp4')
            output_path = os.path.join(output_folder, output_filename)
            convert_webp_to_mp4(input_path, output_path, duration)

    print(f"All .webp files have been converted and saved to {output_folder}.")

# 使用示例
input_folder = 'niubiuniu_by_WuMingv2Bot'
output_folder = 'niubiuniu_by_WuMingv2Bot_mp4'

convert_folder_webps_to_mp4s(input_folder, output_folder, duration=2)
