'''

继承

所有的类的父类都是Object

子类会继承父类的所有属性和方法
可以根据需要重写父类方法

__mro__，继承中查找的顺序，先在子类查找，没有则在父类查找
__base__，查看类的父类
__subclass__，查看子类

overload，重载，可以对不同类型的操作数操作
override，重写，继承中如果不想用父类的方法则可以重写子类的方法

一般继承父类，初始化的时候需要调用父类初始化的方法
如果类没有调用init，默认调用Object的init方法


多态，python中
同一个方法调用，不同子类表现不同的状态
多态的前提是有继承，有方法的覆盖
当传递参数的时候可以传递父类的，然后判断进而调用子类的方法


多继承，有一定的复杂性，有缺点，尽量避免多继承
MRO，当多继承复杂的情况，深度优先有原则


抽象类，一般不用实例化
只定义了接口，不具体实现，要子类实现
1. 子类可以具体实现这些抽象接口，比如Word类
2. 子类不实现抽象接口，定义一个新子类，继承上一个子类，实现这些抽象方法，但是调用的时候需要实例化该子类，比如PDF类
3. 当每个子类需要实现不同的接口，并且有非子类也需要实现某个抽象方法的时，用mixin
   缺什么补什么，可以用装饰器，或者mixin多继承

继承的时候，Mixin类放在子类之前，效果是增强子类功能


'''


class Animal:
    def shout(self):
        print('Animal shouting')


class Dog(Animal):
    # 1. 实现和父类完全不同，不需要调用父类方法
    def shout(self):
        print('Wang Wang')


d = Dog()
d.shout()
print(Dog.__dict__)
print(d.__dict__)


class Cat(Animal):
    # 2. 调用父类的方法
    def shout(self):
        # Animal.shout(self)
        super(Cat, self).shout()
        print('Miao')


print(Animal.__base__)
print(Dog.__base__)
print(Animal.__subclasses__())
print(Dog.__mro__)


c = Cat()
c.shout()
print(Cat.__dict__)
print(c.__dict__)


print('Init'.center(30, '#'))


class A:
    def __init__(self, a):
        self.a = a
        self.__d = 100

    # def show(self):
    #     print(self.a, self.__d)


class B(A):
    def __init__(self, b, c):
        # 继承父类的初始化方法
        super(B, self).__init__(10)
        self.b = b
        self.c = c

    def show(self):
        print(self.a, self.b, self.c)


b = B(2, 3)
b.show()


print('抽象类'.center(30, '#'))


# 抽象类，只定义了抽象的接口，不实现，由具体的子类实现
class Document:
    def __init__(self, content):
        self.content = content

    # 抽象方法
    def printit(self):
        raise NotImplementedError("Please implement yourself")


class Word(Document):
    def printit(self):
        print('[ {} ]'.format(self.content))


class PDF(Document):
    pass


# 用新子类去实现接口
class PrintablePDF(PDF):
    def printit(self):
        print('[ {} ]'.format(self.content))


w = Word('Word string')
w.printit()


p = PrintablePDF('pdf string')
p.printit()

