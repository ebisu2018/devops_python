import os

path = r'E:\迅雷下载\狂飙'
os.chdir(path)
videos = os.listdir(path)
print(videos, os.getcwd())
for name in videos:
    new_name = name.replace('k', '狂')
    # print(new_name)
    os.rename(name, new_name)
