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
print()方法本质就是调用的__str__,str()

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

'''

class A:

    def __bool__(self):
        return False


print(bool(A), bool(A()))


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
实现一个购物车

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

    # 允许通过索引修改
    def __setitem__(self, key, value):
        self.__items[key] = value

    def __add__(self, other):
        return self.__items.append(other)


cart = Cart()
cart.additem('shoe')
cart.additem('phone')
print(len(cart))
print(cart)
for x in cart:
    print(x)

print(cart[1])
cart[0] = 'gun'
print(cart)
