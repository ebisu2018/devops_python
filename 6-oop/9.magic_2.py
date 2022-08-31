'''
容器的魔术方法
实现一个购物车
'''

import time
import datetime
from contextlib import contextmanager

print('container'.center(30, '#'))


class Cart:

    def __init__(self):
        self.__items = []

    # 允许用+添加实例，向实例添加元素
    def __add__(self, other):
        self.__items.append(other)

    # 会调用__add__方法
    def additem(self, item):
        return self + item

    # 返回对象长度，调用len()会执行
    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        return str(self.__items)

    # 允许实例是可迭代，可以对对象遍历
    def __iter__(self):
        yield from self.__items

    # 默认False，in操作符会调用该方法，没有则调用iter的
    def __contains__(self, item):
        if item in self.__items:
            return True

    # 允许通过索引获取元素
    def __getitem__(self, index):
        return self.__items[index]

    # 允许通过索引修改元素
    def __setitem__(self, key, value):
        self.__items[key] = value


cart = Cart()
cart.additem('food')
cart + 'beer'
print(len(cart))
print(cart)

for x in cart:
    print('we have', x)

print('beer' in cart)

cart[0] = 'pizza'
print(cart[0])


print('Callable'.center(30, '#'))

'''

所谓可调用就是对象后面可以加小括号
实例的可调用对象，就是可以在实例后面加小括号
如果要实现实例的可调用，则要实现call方法
callable()判断类或者实例是否可以调用

“instance()”可以理解为是“instance.__call__()”的简写

'''


class A:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 对实例执行调用，会执行__repr__
    def __call__(self, *args, **kwargs):
        return repr(self)

    def __str__(self):
        return 'x:{}, y:{}'.format(self.x, self.y)

    def __repr__(self):
        return 'x-{}, y-{}'.format(self.x, self.y)


a = A(5, 10)
print(a)
print(a())
print(a.__call__())
print('上下文管理'.center(30, '#'))

'''

实例的上下文管理
同时包含 __enter__() 和 __exit__() 方法的对象就是上下文管理器
当 with as 操作上下文管理器时，就会在执行语句体之前
先执行上下文管理器的 __enter__() 方法，然后再执行语句体，最后执行 __exit__() 方法。


__enter__(self)
进入上下文管理器自动调用的方法，该方法会在 with as 代码块执行之前执行，最先执行的是init方法
如果 with 语句有 as子句，那么该方法的返回值会被赋值给 as 子句后的变量
该方法可以返回多个值，因此在 as 子句后面也可以指定多个变量

__exit__（self, exc_type, exc_value, exc_traceback）
退出上下文管理器自动调用的方法
该方法会在 with as 代码块执行之后执行
如果 with as 代码块成功执行结束，程序自动调用该方法，调用该方法的三个参数都为 None
如果 with as 代码块因为异常而中止，程序也自动调用该方法，使用 sys.exc_info 得到的异常信息将作为该方法的参数

常见的有 2 种方式：基于类实现和基于生成器实现
使用基于生成器的上下文管理器时，不再用定义 __enter__() 和 __exit__() 方法，但需要加上装饰器 @contextmanager
无论使用哪一种，不用忘记在__exit__()或者是 finally 块中释放资源


当出现异常时，如果 __exit__ 返回 False（默认不写返回值时，即为 False），则会重新抛出异常，让 with as 之外的语句逻辑来处理异常
如果返回 True，则忽略异常，不再对异常进行处理

上下文应用场景
对函数实现增强，类似装饰器
资源管理
认证

'''


# class A:
#
#     def __init__(self):
#         print('step init')
#
#     def __enter__(self):
#         print('step enter')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('step exit')
#
#
# with A() as a:
#     print('with start')
#     print('with end')

print('基于类的上下文管理器'.center(30, '#'))


class FkResource:
    def __init__(self, tag):
        self.tag = tag
        print(f'初始化 {self.tag}')

    def __enter__(self):
        print(f'__enter__: {self.tag}')
        return self.tag # 返回给as后面的变量

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'__exit__: {self.tag}')
        if exc_tb is None:
            print('没有异常时关闭资源')
        else:
            print('遇到异常时关闭资源')
            return True


with FkResource('孙悟空') as dr:
    print('dr:', dr)
    print('[with代码块] 没有异常')


with FkResource('白骨精'):
    print('[with代码块] 异常之前的代码')
    raise Exception
    print('[with代码块] ~~~~~~~~异常之后的代码')
print('基于生成器的上下文管理器'.center(30, '#'))


@contextmanager
def file_manager(name, mode):
    try:
        f = open(name, mode)
        yield f
    finally:
        f.close()


with file_manager('test', 'w') as f:
    f.write('hello world')


# class Timeit:
#     def __enter__(self):
#         self.start = datetime.datetime.now()
#         print('开始计时')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         delta = (datetime.datetime.now() - self.start).total_seconds()
#         print(f'took {delta}s')
#
#
# def add(a, b):
#     time.sleep(1)
#     return a + b
#
#
# with Timeit() as t:
#     add(4, 6)


class ListDemo:
    def __init__(self):
        self.__date = []
        self.__step = 0

    def __next__(self):
        if self.__step <= 0:
            raise StopIteration
        self.__step -= 1
        return self.__date[self.__step]

    def __iter__(self):
        return self

    def __setitem__(self, key, value):
        self.__date.insert(key, value)
        self.__step += 1


myList = ListDemo()
myList[0] = 1
myList[1] = 2
for i in myList:
    print(i)
