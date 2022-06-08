'''

生成器表达式只能写简单的表达式，由一条表达式构成
如果需要构建复杂的函数，则用生成器函数

生成器函数
函数生成的依然是生成器对象! 不会直接返回结果，调用next后会返回一个值
如果用next方法，碰到return后会抛出异常
如果有多个yield，每一次会暂停在yield处
可以构建出无限个元素的容器
yield可以一次或者多次，但最好是多次，一次还不如用return

生成器对象特点：
也属于可迭代对象
惰性，需要的时候才计算，不会立即占用内存
不可用索引
有next()方法
只能迭代一次

生成器对象构造：
1 生成器表达式 (i for i in range(n))
2 有yield关键字的生成器函数

'''


def gen():
    for i in range(5):
        yield i + 1


g = gen()
print(gen)
print(gen()) # 返回的是generator

for i in g:
    print(i)

def foo():
    yield 9
    yield 8
    yield 7
    return 6

for i in foo():
    print(i)


# 构造无限个元素的容器
def foo():
    def bar():
        count = 0
        while True:
            count += 1
            yield count
    c = bar() # 返回生成器对象
    return lambda: next(c) #lambda返回对生成器的next方法

x = foo()
print(x)
print(x())
print(x())


# 生成器函数的斐波那契数列
def fib():
    a = 1
    yield a
    b = 1
    yield b
    while True:
        a, b = b, a + b
        yield b


f = fib()
for i in range(10):
    print(i + 1, next(f))



