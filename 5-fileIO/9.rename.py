import os

path = r'E:\Movies\越狱第一季'
os.chdir(path)
videos = os.listdir(path)
print(videos, os.getcwd())
for name in videos:
    new_name = name.replace('.BD1080p', '')
    # print(new_name)
    os.rename(name, new_name)
