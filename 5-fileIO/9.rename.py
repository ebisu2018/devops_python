import os

path = r''
os.chdir(path)
videos = os.listdir(path)
print(videos, os.getcwd())
for name in videos:
    new_name = name.replace('', '')
    # print(new_name)
    os.rename(name, new_name)
