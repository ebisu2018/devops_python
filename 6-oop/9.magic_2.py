'''
容器的魔术方法
实现一个购物车
'''

import time
import datetime

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
当使用with对实例进行上下文管理时
需要实现enter和exit方法

__enter__()，进入上下文，with会把此方法返回值赋值给as的变量
__exit__()，退出对象的上下文时执行

上下文应用场景
对函数实现增强，类似装饰器
资源管理
认证

'''


class A:

    def __init__(self):
        print('step init')

    def __enter__(self):
        print('step enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('step exit')


# with A() as a:
#     print('with start')
#     print('with end')


class Timeit:
    def __enter__(self):
        self.start = datetime.datetime.now()
        print('开始计时')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        delta = (datetime.datetime.now() - self.start).total_seconds()
        print(f'took {delta}s')


def add(a, b):
    time.sleep(1)
    return a + b


with Timeit() as t:
    add(4, 6)
