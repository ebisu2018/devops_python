'''
获取脚本命令行的参数方法

sys.argv，返回一个列表，依次是脚本名，参数值

如果想命令行的参数进行解析需要使用argparse模块

ArgumentParser()生成一个argparse对象，默认程序名是脚本名字

add_argument增加位置参数
如果没有nargs表示位置参数，每次是必须写的参数

如果要表示非必须位置参数，就是位置参数可有可无，则用nargs
nargs后面
+ 至少1个，不能有default
？0或1个，可以有default
* 任意个，可以有default

store_true，表示有选项参数则是true，反之是false
parse_args()，返回的是参数解析的对象，是一个NameSpace()


'''

import sys
import argparse

print(sys.argv)

parser = argparse.ArgumentParser('ls', description="show files list", add_help=True)

# 增加positional arguments
parser.add_argument('param', nargs='?', default='.', help="dir name")
# parser.add_argument('param2', default='.', nargs='?')
# parser.add_argument('param3', default='.', nargs='*')

# 增加optional arguments，store true来表示bool
parser.add_argument('-a', '--all', action='store_true', help="show all")
parser.add_argument('-f', action='store_false', help="store false")

# 打印帮助
parser.print_help()

# 解析参数，一般不会写列表传入，从命令行接收，这里仅是测试
args = parser.parse_args(['/etc', '-af'])
print(type(args), args)

# 获取参数值
print(args.param, args.all, args.f)

