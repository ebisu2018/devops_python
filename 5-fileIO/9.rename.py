import os

path = r'E:\迅雷下载\斯巴达克斯第一季'
os.chdir(path)
videos = os.listdir(path)
print(videos, os.getcwd())
for name in videos:
    new_name = name.replace('[www.mp4kan.com]s巴d克s', '斯巴达克斯')
    # print(new_name)
    os.rename(name, new_name)
