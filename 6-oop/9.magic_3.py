'''
反射
在运行时获取类型定义信息

通过一个对象，找到type，class，attribute或method
可以使用字符串属性来调用getattr或者setattr进行取值和赋值
hasattr来判断是否包含属性

其中属性都是用字符串表示

hasattr() 函数的用法，该函数的功能是查找类的实例对象中是否包含指定名称的属性或者方法
但该函数有一个缺陷，即它无法判断该指定的名称，到底是类属性还是类方法
可以结合使用__call__弥补

'''


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(10, 20)
# 通过get获取属性值
print(getattr(a, 'x'))
# 在类外面，通过set动态创建方法
setattr(A, 'showme', lambda self: '{}, {}'.format(self.x, self.y))
print(getattr(a, 'showme')())
# 判断对象是否有属性
print(hasattr(a, 'x'))
print(hasattr(a, 'showme'))


class CLanguage:
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"

    def say(self):
        print("我正在学Python")


clangs = CLanguage()
if hasattr(clangs, "name"):
    print(hasattr(clangs.name, "__call__"))
print("**********")
if hasattr(clangs, "say"):
    print(hasattr(clangs.say, "__call__"))
print('反射'.center(30, '#'))

'''

反射的魔术方法，重要！！
注意需要调用父类的方法！

__getattribute__: 属性访问第一站，比__dict__访问还要早
如果需要对属性包装可以调用该方法
不建议调用，要调用父类的方法！
return的值是属性查找的结果
如果抛出AttributeError则会调用__getattr__

__getattr__
当没有找到属性会调用该方法
用于拦截AttributeError，使其不抛出AttributeError异常
如果在子类以及父类的__dict__中找不到属性，会调用该方法，可以返回一个值，而不会抛出AttributeError

__setattr__
如果有setattr()或者实例.属性或者实例进行初始化赋值会触发该方法
如果方法中依然用实例.属性赋值，则会产生递归！
因此调用父类的或者用__dict__方式赋值！

__delattr__
del 实例.属性，会触发__delattr__，不常用


实例属性的查找顺序
__getattribute__, instance.__dict__, instance.__class__.__dict__, object.__dict__, __getattr__

'''


class B:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 没找到属性会调用
    def __getattr__(self, item):
        return f"calling __getattr__: {item} not exists!"

    # 属性赋值时调用
    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        # 或者用字典的方式赋值
        # self.__dict__[key] = value
        print(f'calling __setattr__: {key} : {value}')

    # 删除属性,调用的方法
    def __delattr__(self, item):
        super().__delattr__(item)
        print(f'calling __delattr__: {item}')

    def __getattribute__(self, item):
        print(f'calling __getattribute__: {item}')
        return super().__getattribute__(item)


# 初始化也会调用__setattr__
b = B(100, 200)
# 属性不存在，会调用getattr方法！
print(b.a)
# 调用__setattr__
b.a = 200
# 删除会调用__delattr__
del b.a

print(b.x)
