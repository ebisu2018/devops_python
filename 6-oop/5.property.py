'''

属性装饰器

私有变量尽量不要在外层访问，最好封装一个setter()和getter()，而是避免直接使用属性

如果不想用getter和setter的方法赋值属性，可以使用property装饰器
方法名字必须和属性名字相同
在getter的方法上加上@property
在setter的方法上加上@name.setter
条件：名字必须相同，和属性名一样！
好处：看似访问的属性，但背后是函数，更加强大

如果想保留getter和setter，可以使用property方法，把getter和setter传入，赋值给属性
就可以用属性方式调用

'''


class Person:
    def __init__(self, name):
        self._name = name

    # getter
    def get_name(self):
        return self._name

    # setter
    def set_name(self, name):
        self._name = name

    name = property(get_name, set_name)


tom = Person('tom')
tom.name('tommy')
print(tom.get_name())
print(tom.name)


class Dog:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


huanhuan = Dog('huanhuan')
huanhuan.name = 'qiuqiu'
print(huanhuan.name)