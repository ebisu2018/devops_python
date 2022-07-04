'''


访问控制

1. Public: 就是普通定义的属性或者方法；任何地方都可以访问
2. Private: __属性，表示私有的，外部访问不到该变量，仅在类内部访问，在类内部是 _类__属性名 构成
因此虽然是隐藏的，但是通过这种方式也是可以访问
理想的做法是通过其他public接口暴露这些private
3. Protected：_属性，表示被保护的，python中并没有只是社区规定的，在类或者子类中使用，是一种约束

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