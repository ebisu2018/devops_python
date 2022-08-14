'''

lambda 匿名函数，没有名字的函数
常用来表示内部仅包含 1 行表达式的函数
如果一个函数的函数体仅有 1 行表达式

定义并调用
(lambda 形参: 返回内容)(实参)

'''

# 定义
fn = lambda x: x ** 2
print(fn)

# 调用
print(fn(10))

# 定义和调用，传参和普通函数一样！
print((lambda x, y=10: x + y)(5))

print((lambda x, /, *, y: x * y)(5, y=10))

print((lambda *args: [i for i in args])(*range(5)))

print((lambda *args: (i for i in args))(*range(5)))


# 创建一个defaultdict，如果有KeyError的错误，则会以key创建一个value，值为参数中指定的默认类型
from collections import defaultdict

d = defaultdict(list)
d['d1'].extend(range(5))
print(d)

d2 = defaultdict(lambda: {100})
print(d2['d2'])

d3 = defaultdict(lambda: list())
print(d3['d3'])
