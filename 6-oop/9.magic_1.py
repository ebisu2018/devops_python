'''

面向对象的魔术方法

构造实例的过程：
__new__(): 构造实例，从无到有，返回一个instance，一般不需要调用
返回一个object基类构造出的实例模版！
如果返回的不是cls的实例，则init方法不会被调用！

__init__(): 返回实例后会调用初始化方法得到一个初始化好的实例


'''

print('实例化'.center(30, '#'))


class A:
    def __new__(cls, *args, **kwargs):
        print('cls是', cls)
        print(args, kwargs)
        return super().__new__(cls)

    def __init__(self, x, y):
        print('init')
        self.x = x
        self.y = y


a = A(5, 10)
print(a, type(a))

print('可视化'.center(30, '#'))

'''
自定义对象的描述
__str__, 返回的是对象的描述的字符串表示，必须返回的是字符串
直接调用的时候使用，如果没有重写__str__，调用__repr__，如果也没有定义则返回内存地址信息

__repr__，如果间接展示的调用的是repr方法，如果没有则调用__str__的，仍然没有则调用object的内存地址

'''


class A:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f'用str表达就是：x = {self.x}'

    def __repr__(self):
        return f'用repr表达就是：<name> is {self.x}'


a = A(10)
print(a)
print((a,))


print('bool类型'.center(30, '#'))

'''

bool类型
如果对实例进行bool判断则需要实现

'''


class B:

    def __bool__(self):
        return False


print(bool(B()))

'''

运算符重载
实例之间的比较需要实现比较的魔术方法
==如果没有实现默认会调用object的is，判断地址

'''

print('运算符重载'.center(30, '#'))


class C:

    def __init__(self, num):
        self.num = num

    # 大于
    def __gt__(self, other):
        return self.num > other.num

    # 大于等于
    def __ge__(self, other):
        return self.num >= other.num

    # 小于
    def __lt__(self, other):
        return self.num < other.num

    # 小于等于
    def __le__(self, other):
        return self.num <= other.num

    # 等于
    def __eq__(self, other):
        return self.num == other.num

    # 不等于
    def __ne__(self, other):
        return self.num != other.num


w = C(26)
d = C(34)
print(w < d)
print('数学运算'.center(30, '#'))


'''

实例之间做数学运算用的魔法方法
比如datetime的模块可以用实例对时间进行运算

'''


class D:

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __isub__(self, other):
        pass
