import os

path = r'E:\Download\鸡皮疙瘩系列'
os.chdir(path)
videos = os.listdir(path)
print(videos, os.getcwd())
for name in videos:
    new_name = name.replace('[迅雷下载www.2tu.cc]', '')
    # print(new_name)
    os.rename(name, new_name)
