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
import random
from string import ascii_lowercase

base = Path()
sub = Path('b/c/d/e')
dirs = [sub] + list((base / sub).parents)[:-1]
# print(dirs)

if sub.exists():
    shutil.rmtree((base / 'b'))

if Path('dest').exists():
    shutil.rmtree((base / 'dest'))

(base / sub).mkdir(parents=True, exist_ok=True)

for i in range(10):
    name = ''.join(random.choices(ascii_lowercase, k=4))
    (random.choice(dirs) / name).touch()

headers = set('xyz')


def ignore_files(src, names):
    print('src is {}'.format(src))
    print('names is {}'.format(names))
    return set(filter(lambda name: name[0] not in headers and Path(src, name).is_file(), names))


shutil.copytree((base / 'b'), (base / 'dest'), ignore=ignore_files)

print(*(base / 'dest').rglob('*'), sep='\n')
