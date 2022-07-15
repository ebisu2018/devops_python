'''

面向对象的魔术方法

构造实例的过程：
__new__(): 构造实例，从无到有，返回一个instance，不需要调用
返回一个object基类构造出的实例模版

__init__(): 返回实例后会调用初始化方法得到一个初始化好的实例


'''


class A:
    def __new__(cls, *args, **kwargs):
        print('cls是', cls)
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, x, y):
        print('init')
        self.x = x
        self.y = y


a = A(5, 10)
print(a, type(a))


'''
自定义对象的描述
__str__, 返回的是对象的描述的字符串表示，必须返回的是字符串
直接调用的时候使用，如果没有重写__str__，则执行父类的__str__
print()和str()方法本质就是调用的__str__

__repr__，如果间接展示的调用的是repr方法，如果没有则调用__str__的，仍然没有则调用object的

'''

class A:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f'x = {self.x}'

    def __repr__(self):
        return f'<name> is {self.x}'


a = A(10)
print([a, str(a), (a,), repr(a)])

'''

bool类型
如果对实例进行bool判断则需要实现

'''

class A:

    def __bool__(self):
        return False


'''

运算符重载
实例之间的比较需要实现比较的魔术方法
==如果没有实现默认会调用object的is，判断地址

'''

class A:
    # 大于
    def __gt__(self, other):
        pass

    # 大于等于
    def __ge__(self, other):
        pass

    # 小于
    def __lt__(self, other):
        pass

    # 小于等于
    def __le__(self, other):
        pass

    # 等于
    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass


'''

实例之间做数学运算用的魔法方法
比如datetime的模块
可以对实例进行相加相减操作

'''

class A:

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __isub__(self, other):
        pass


'''

要实现容器的魔术方法
比如实现一个购物车

'''


class Cart:
    def __init__(self):
        self.__items = []

    # 会调用__add__方法
    def additem(self, item):
        return self + item

    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        return str(self.__items)

    # 允许实例是可迭代
    def __iter__(self):
        yield from self.__items

    # in 操作符会调用该方法，没有则调用iter的in方法
    def __contains__(self, item):
        pass

    # 允许索引获取元素
    def __getitem__(self, index):
        return self.__items[index]

    # 允许通过索引修改元素
    def __setitem__(self, key, value):
        self.__items[key] = value

    # 允许向实例添加元素
    def __add__(self, other):
        return self.__items.append(other)


# cart = Cart()
# cart.additem('shoe')
# cart.additem('phone')
# print(len(cart))
# print(cart)
# for x in cart:
#     print(x)
#
# print(cart[1])
# cart[0] = 'gun'
# print(cart)


'''

实例的可调用对象
如果要实现实例的可调用，则要实现call方法

callable()判断类或者实例是否可以调用

'''

class A:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        return repr(self)

    def __str__(self):
        return 'x:{}, y:{}'.format(self.x, self.y)

    def __repr__(self):
        return 'x-{}, y-{}'.format(self.x, self.y)


# a = A(5, 10)
# print(a)
# print(a())


'''

实例的上下文管理
当使用with对实例进行上下文管理时
需要实现enter和exit方法

如果想在start之前做一些增强可以放到enter中
类似装饰器的道理

'''

class A:

    def __init__(self):
        print('step init')

    def __enter__(self):
        print('step enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('step exit')


# with A():
#     print('with start')
#     print('with end')


'''

反射
通过一个对象，找到type，class，attribute或method
可以使用字符串属性来调用getattr或者setattr进行取值和赋值
hasattr来判断是否包含属性

类中的魔术方法
__getattribute__: 属性访问第一站，比__dict__访问还要早
如果需要对属性包装可以调用该方法
不建议调用，要调用父类的方法！

__getattr__
用于拦截AttributeError的
如果在父类的__dict__中依然找不到属性，会调用该方法，可以返回一个值，而不会抛出AttributeError

__setattr__
如果有setattr()或者实例.属性，都会触发该方法
如果方法中依然用实例.属性赋值，则会产生递归
一般调用父类的或者用字典方式赋值

del 实例.属性，会触发__delattr__，不常用


'''

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 没有找到属性的时候会调用
    def __getattr__(self, item):
        return None

    # 属性赋值的时候会调用
    # def __setattr__(self, key, value):
    #     super().__setattr__(key, value)
        # 或者用字典的方式赋值
        # self.__dict__[key] = value

    # 删除属性,调用的方法
    # def __delattr__(self, item):
    #     super().__delattr__(item)

    def __getattribute__(self, item):
        return super().__getattribute__(item)


a = A(10, 20)
# print(getattr(a, 'x'))
# print(getattr(a, 'y'))
# 在类外面动态创建方法,调用方法
# setattr(A, 'showme', lambda self: '{}, {}'.format(self.x, self.y))
# print(getattr(a, 'showme')())
# 判断对象是否有属性
# print(hasattr(a, 'a'))

print(a.x, a.a, a.__dict__)
