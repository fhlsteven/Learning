# -*- coding: utf-8 -*-
import os
import subprocess
import time

def get_video_duration(video_path):
    ext = os.path.splitext(video_path)[-1]
    if ext != '.mp4' and ext != '.avi' and ext != '.flv':
        raise Exception('format not support')
    ffprobe_cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'
    p = subprocess.Popen(
        ffprobe_cmd.format(video_path),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)
    out, err = p.communicate()
    duration_info = float(str(out, 'utf-8').strip())
    return int(duration_info)

'''
ffmpeg：是一个开源的音视频处理工具，用于处理、转换和流媒体解决方案。
-ss：指定开始裁剪的时间点。在这里，ss 应该是一个时间点的字符串，如 "00:01:30"，表示从视频的 1 分钟 30 秒处开始裁剪。
-t：指定裁剪的持续时间。t 应该是一个时间段的字符串，如 "00:02:00"，表示裁剪 2 分钟的视频内容。
-accurate_seek：精确寻找模式，用于在指定时间点开始处理。
-codec copy：使用原始视频和音频编解码器进行拷贝，以保持原始数据的质量和速度。
-avoid_negative_ts 1：避免生成负时间戳。在进行时间戳处理时，确保输出文件的时间戳不会出现负值。
'''
def del_se(dir_path, batch_size=10):
    print('-- del_se start -- ' + dir_path)
    output_folder = '../dldldel/'

    # 确保输出文件夹存在，如果不存在则创建
    os.makedirs(output_folder, exist_ok=True)

    input_dir_path = os.path.abspath(dir_path)
    output_dir_path = os.path.abspath(output_folder)

    # 遍历输入文件夹中的所有MP4文件
    for filename in os.listdir(dir_path):
        if filename.endswith('.mp4'):
            vpath = os.path.join(input_dir_path,filename)
            duration = get_video_duration(vpath)

            topath = os.path.join(output_dir_path, filename)

            # -accurate_seek -i
            cmd = f'ffmpeg -i {vpath} -ss 00:02:00 -to {duration-90} -codec copy -avoid_negative_ts 1 -loglevel quiet {topath}'

            re = os.system(cmd)

            time.sleep(5)
            print(f'cmd:{cmd},result:{re}')

            print(f'{filename} 处理完成.{duration}')

    print('-- del_se end --')

if __name__ == '__main__':    
    del_se('./dldl2019/')