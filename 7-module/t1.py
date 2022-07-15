'''

dir()，当前作用域的所有变量，是变量名列表，参数可以有对象，查看对象的属性和变量
globals()是当前模块全局的变量，是kv的字典
locals()是当前作用域的局部变量，是kv的字典

import的作用：提供一个全局标识符，指向模块对象，通过标识符找对应模块
import导入的必须module类型（py文件或目录），不可以是函数，类或者其他
from <module> import <class, module, func, var, *>

import一个顶级模块，会将顶级模块加入名称空间使用
import一个非顶级模块，如os.path，只会将顶级模块加入名称空间，使用必须使用限定的名称
import...as 别名，别名加入名称空间

导入模块会执行模块的顶层代码，会执行类，函数，变量
导入的标识符是当前模块的，只是指向了模块对象
每个模块只执行一次

模块加载在sys.module中,以字典的形式
如果没有找到，则在sys.path()查找，是python查找模块的路径

例子
from m import x
不能用m.的方式获取其他，因为本地变量只有x
但是module中会加载from中的模块

import m
最小化使用m中的变量，不可以使用m下的子模块

import m.m1
可以使用m以及m.m1，父模块和子模块都会被加载

模块是最小化加载原则
导入子模块一定会加载父模块，加载父模块一定不会加载子模块
模块要用必须加载，如果加载包可以使用__init__中的
import代表加载，在sys.module中，使用的变量在dir()中，2者不是一个概念
如果要使用模块的资源，必须确保sys.module中有该模块！


相对路径的导入不要用在包之外，一般在包内使用
加载模块是加载模块，还要清楚模块有哪些标识符可以使用(dir())

'''

import t2
import sys
import os
from m1 import m2

print(dir())

# 加载模块的顺序，先从工作目录中查找，没有再去标准库中
# print(*sys.path, sep='\n')
# print(*sys.modules.items(), sep='\n')

# print(*filter(lambda x: x.startswith('m'), sys.modules.keys()))


# 执行当前模块__name__是__main__
# if __name__ == '__main__':
#     print('我是', __name__)
#     print(__file__)

