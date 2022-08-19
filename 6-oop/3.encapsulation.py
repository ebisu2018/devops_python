'''

封装（Encapsulation）
即在设计类时，刻意地将一些属性和方法隐藏在类的内部
这样在使用此类时，将无法直接以“类对象.属性名”（或者“类对象.方法名(参数)”）的形式调用这些属性（或方法）
而只能用未隐藏的接口间接操作这些隐藏的属性和方法


访问控制
通过__dict__可以查看到

1. Public: 就是普通定义的属性或者方法；任何地方都可以访问
2. Private: __属性，表示私有，只能在本类内部使用，类的外部以及子类都无法使用
在类内部是 _类名__属性（方法） 构成，因此虽然是隐藏的，但是通过这种方式也是可以访问
理想的做法是通过其他public接口暴露这些private
3. Protected：_属性，表示被保护的，python中并没有，只是社区规定，在类或者子类中使用，是一种约束

'''


# Private
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def info(self):
        print(f'{self.__name} is {self.__age}')


p = Person('Jack', 28)
p.info()
print(p.__dict__)
print(p._Person__name)


# protected
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def info(self):
        print(f'{self._name} is {self._age}')


p = Person('Tony', 28)
p.info()
print(p.__dict__)
print(p._name)
