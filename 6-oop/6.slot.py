'''

允许为 类 动态地添加实例，类，静态方法
但对于实例对象，则只允许动态地添加实例方法，不能添加类方法和静态方法

__slots__ 属性，通过它可以避免用户频繁的给实例对象动态地添加属性或方法
__slots__ 属性值其实就是一个元组，只有其中指定的元素，才可以作为动态添加的属性或者方法的名称
__slots__ 属性只对当前所在的类起限制作用

type可以创建动态类
type(name, bases, dict)
name 表示类的名称；bases 表示一个元组，其中存储的是该类的父类；dict 表示一个字典，用于表示类内定义的属性或者方法

'''


class CLang:
    pass


def info(self):
    print('实例方法')


@classmethod
def info2(cls):
    print('类方法')


@staticmethod
def info3():
    print('静态方法')


CLang.info = info
CLang.info2 = info2
CLang.info3 = info3
print(CLang.__dict__)
clang = CLang()
clang.info()
clang.info2()
clang.info3()

clang1 = CLang()
clang1.info = info
clang1.info(clang1)


class PLanguage:
    __slots__ = ('name', 'add', 'info')


plang = PLanguage()
plang.name = 'python'

print('type创建动态类'.center(30, '#'))


def learn(self):
    print("我要学Python")


PLanguage = type('Planguage', (object,), dict(learn=learn, name='python.org'))
plang = PLanguage()
print(plang.name)
plang.learn()
print(plang.__dict__)
