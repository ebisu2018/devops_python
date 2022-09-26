import os

path = r'F:\迅雷下载\宇宙时空之旅'
os.chdir(path)
videos = os.listdir(path)
print(videos, os.getcwd())
for name in videos:
    new_name = name.replace('[www.domp4.cc]宇z时k之l', '宇宙时空之旅')
    # print(new_name)
    os.rename(name, new_name)