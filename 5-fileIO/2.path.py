'''

目录树
磁盘中存储是物理的
文件系统是逻辑的，为了人方便查找读取

os.path()是基础的库
pathlib是高级的库，更方便

拼接路径必须注意根'/'的位置，位于首位
其他不需要加/，会自动添加

'''

import os.path
from pathlib import Path

cwd = os.getcwd()
print('当前工作目录是:', cwd)

# 拼凑路径，只在根加斜杠，其他不加，如果其他的有根，则前面的会忽略
p = os.path.join('/etc', 'sysconfig', 'test')
print(p)

# 获取basename
print('basename:', os.path.basename(p))

# 获取目录
print('dirname:', os.path.dirname(p))

# 判断文件是否存在
print('Exists:', os.path.exists(p))

# 是否是绝对路径，前面必须有根才是
print('isabs:', os.path.isabs(p))

# 把dir和basename分在一个元组中
print('split:', os.path.split(p))

# 区分出路径和后缀
print(os.path.splitext('/etc/sysconfig/mysql.tar.gz'))

# 根据当前文件生成绝对路径
print('abspath:', os.path.abspath('test'))

# 获取当前模块的名字和路径
print(__name__, __file__)

# 获取当前模块所在目录
parent = os.path.dirname(__file__)
print('dir:', parent)

print('base:', os.path.basename(__file__))

print('isfile:', os.path.isfile(__file__))

print('isdir:', os.path.isdir(cwd))

print('Pathlib'.center(30, '#'))

#
#
# # 获取当前的相对路径和绝对路径
# print(Path(), Path(''), Path('.'), Path().absolute())
#
# # 拼接路径字符串
# p = Path('/usr', 'bin', 'local')
# print(p, type(p), str(p))
#
# # 可以嵌套Path对象
# print(Path('/etc', Path('sysconfig', 'network')))
#
# # /可以和Path对象结合重载为路径拼接
# print(Path('/etc') / 'conf')
#
# # 把各个路径分隔放到元组中
# print(p.parts)
#
# # 获取父目录
# p = Path('/a/b/c/d/e/f/g')
# print(p.parent.parent.parent)
#
# # 拼接新路径，和Path()拼路径一样
# jp = p.joinpath('1/2/3', Path('x/y/z/mysql.gz'))
# print(jp)
#
# # 获取basename
# print(jp.name)
#
# # 获取文件后缀
# print(jp.suffix)
#
# # 除去后缀的文件名
# print(jp.stem)
#
# # 之前路径的文件名替换别名
# print(jp.with_name('nginx.tar'))
#
#
# # 返回所有父目录，遍历可以取出
# # for i in p.parents:
# #     print(i)
#
# # 获取绝对路径，文件不一定非要存在
# print(Path(__file__).absolute())
# print(Path('test').absolute())
# print(p.absolute())
#
# # 获取家目录
# print(Path.home())
# print(jp.home())
#
# # 获取当前工作目录
# print(Path.cwd())
#
# # 判断是否存在
# print(p.exists())
#
# print(p.is_dir())
#
# # 创建文件夹, parents表示父目录必须存在，exist ok表示有目录不会提示
# p = Path('a/b')
# p.mkdir(parents=True, exist_ok=True)
#
# # 创建文件
# (p / 'nginx.tar').touch()
#
# # 遍历Path对象，不会递归查找
# for i in p.iterdir():
#     print(i)
#
#
# # 匹配当前路径下所有的内容，不会递归
# print(list(Path().glob('*')))
#
# # 递归调用
# print(list(Path().glob('**/*')))
#
# # 匹配路径下所有的文件，等同于**/*，会递归查询，返回相对路径，这种方式效率不高
# print(list(Path().rglob('*.tar')))
