import os

path = r'F:\迅雷下载\1899.s01'
os.chdir(path)
videos = os.listdir(path)
print(videos, os.getcwd())
for name in videos:
    new_name = name.replace('.HD中字[66影视www.66Ys.Co]', '')
    # print(new_name)
    os.rename(name, new_name)
