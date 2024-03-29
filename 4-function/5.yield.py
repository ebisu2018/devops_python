'''

生成器表达式只能写简单的表达式，由一条表达式构成 (i for i in range(n))
如果需要构建复杂的函数，则用生成器函数

生成器的创建方式：
定义一个以 yield 关键字标识返回值的函数
调用刚刚创建的函数，即可创建一个生成器

即便调用生成器函数，Python 解释器也不会执行函数中的代码，它只会返回一个生成器（对象）

生成器函数
函数生成的依然是生成器对象! 不会直接返回结果，调用next后会返回一个值
如果用next方法，碰到return后会抛出异常
如果有多个yield，每一次会暂停在yield处
可以构建出无限个元素的容器
yield可以一次或者多次，但最好是多次，一次还不如return

生成器对象特点：
也属于可迭代对象
惰性，需要的时候才计算，不会立即占用内存
不可用索引
有next()方法
只能迭代一次

生成器对象构造：
1 生成器表达式 (i for i in range(n))
2 有yield关键字的生成器函数

函数因为有了yield可以中断函数执行，期间执行另一个函数的yield，协程的本质

yield是返回一个惰性的对象
yield from后面跟的是一个可迭代对象，可以用map的方式一一取出

'''


def gen():
    for i in range(5):
        yield i + 1


g = gen()
print(gen)
print(gen()) # 返回的是generator

# for里面会自动调用next方法
for i in g:
    print(i, end=' ')

print()
print('yield多个'.center(30, '#'))


def foo():
    yield 9
    yield 8
    yield 7
    return 6


for i in foo():
    print(i, end=' ')

print()


# 构造无限个元素的容器
def foo():
    def bar():
        count = 0
        while True:
            count += 1
            yield count
    c = bar()  # 返回生成器对象
    return lambda: next(c)  #lambda返回对生成器的next方法


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

print('yield from'.center(30, '#'))


def foo():
    yield from range(20, 26)


for i in foo():
    print(i)

print('yield from with map'.center(30, '#'))


def bar():
    yield from map(lambda x: x + 1, range(10, 16))


# 协程
f = foo()
b = bar()
for i in range(5):
    print(next(f))
    print(next(b))


def intNum():
    print('开始执行')
    for i in range(5):
        yield i
        print('继续执行')


num = intNum()
print(num)
print(next(num))
print(num.__next__())
for i in num:
    print(i)


def foo():
    bar_a = yield "hello"
    bar_b = yield bar_a
    yield bar_b


f = foo()
print(f.send(None))
print(f.send('Test'))
