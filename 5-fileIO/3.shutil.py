'''

shutil模块和shell相关的都在这里
copyfileobj，是核心，操作文件对象，复制内容
copyfile，判断文件是否相等，调用copyfileobj
copy，copyfile复制内容，copymode复制权限
copy2，copyfile复制内容，copystat复制权限和其他元数据
copytree，复制目录

'''

import shutil
from pathlib import Path


