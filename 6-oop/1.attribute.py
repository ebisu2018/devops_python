'''

面向对象
三个要素：
封装，只暴露该暴露的接口，其他复杂的接口可以在内部存在，不必暴露的封装起来
继承，解决复用的问题，继承父类即可
多态，动态绑定

类名使用大写，类名是一个标识符，指向类对象，在堆内存中

实例
每次实例化都是构造的不同的实例
self，指当前实例本身

实例化过程：
1 完成实例构造 __new__()，不需要显示调用
2 调用init方法初始化实例 __init__()，默认调用父类
返回一个实例

如果不写init方法，会调用父类的初始化方法

实例方法中第一个参数都是self，代表实例本身
方法绑定：实例.方法()方式，解释器会自动注入实例到方法的'self'中

类属性，是所有实例共享的，放在类的__dict__中
实例属性，是每个属性自己的，放在实例的__dict__中，通过self访问

属性访问规律：
1.  通过实例.属性，优先访问实例自己的字典，没有则在类的字典中查找
如果两者字典中都没有，则抛出AttributeError
2. 如果通过实例.__dict__[attribute]方式访问属性，如果实例字典中没有则直接抛出AttributeError
不会向上查找类的__dict__

可以通过实例访问类，实例.__class__
但是通过类不能访问到实例！

'''

class Person:
    # 文档
    """Class Doc"""
    # 类属性
    x = 123
    y = 'abc'

    # 类方法
    def eat(self):
        print('eat', __class__.__name__)

# print(__name__)
# print(__file__)
print(Person, Person.__doc__, Person.__name__)
print(Person.x, Person.y, Person.eat)


class Person:

    color = 'red'
    # 初始化
    def __init__(self, name, age):
        self.name = name # 实例属性
        self.age = age # 实例属性
        print('init method')

    def intro(self):
        print(f'{self.name} is {self.age}')


# 实例化
p = Person("Tom", 25)
print(p, p.name, p.age)
p.intro()

# 类的类是元类
print(Person.__class__, Person.__class__.__name__) # <class 'type'> type

# 等同于__class__
print(type(Person), type(Person).__name__) # <class 'type'> type

# 实例的类型是类
print(type(p), p) # <class '__main__.Person'> <__main__.Person object at 0x7faa50113c40>

# 等同于type
print(p.__class__, p.__class__.__name__) # <class '__main__.Person'> Person

# 保存类属性和方法
print(Person.__dict__)

# 实例字典，保存实例属性
print(p.__dict__)

