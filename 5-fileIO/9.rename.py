import os

path = r'E:\迅雷下载\马大帅1'
os.chdir(path)
videos = os.listdir(path)
print(videos, os.getcwd())
for name in videos:
    new_name = name.replace('[www.mp4kan.com]m大s', '马大帅')
    # print(new_name)
    os.rename(name, new_name)
