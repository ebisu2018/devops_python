'''

描述符
通过使用描述符，可以在引用一个对象属性时自定义要完成的工作
__set__(self, obj, type=None)：在设置属性时将调用这一方法
__get__(self, obj, value)：在读取属性时将调用这一方法
实现了 setter 和 getter 方法的描述符类被称为数据描述符
如果只实现了 getter 方法，则称为非数据描述符


属性装饰器

访问类属性的方式
1 类对象.属性
2 用“类对象.属性”的方式访问类中定义的属性，这种做法破坏了类的封装原则
正常情况下，类包含的属性应该是隐藏私有的，只允许通过类提供的方法来间接实现对类属性的访问和操作
私有变量尽量不要在外层访问，最好封装一个setter()和getter()，而是避免直接使用属性！
属性用_表示私有，然后提供getter和setter方法
3 property() 函数，可以实现在不破坏类封装原则的前提下，让开发者依旧使用“类对象.属性”的方式操作类中的属性
属性名=property(fget=None, fset=None, fdel=None, doc=None)
第一个参数必须是getter，第二个是setter

如果不想用getter和setter的方法赋值属性，可以使用property装饰器
方法名字必须和属性名字相同
在getter的方法上加上@property
在setter的方法上加上@name.setter
条件：名字必须相同，和属性名一样！
好处：看似访问的属性，但背后是函数，更加强大

如果想保留getter和setter，可以使用property方法，把getter和setter传入，赋值给属性
就可以用属性方式调用

'''

print('描述符'.center(30, '#'))


class RevealAccess:
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print('Retrieving', instance, owner, self.name)
        return self.val

    def __set__(self, instance, value):
        print('updating', instance, value, self.name)
        self.val = value


class MyClass:
    x = RevealAccess(10, 'var "x"')
    y = 5


m = MyClass()
print(m.x)
m.x = 20
print(m.x)

print('Property()'.center(30, '#'))


class Person:
    def __init__(self, name):
        self._name = name

    # getter
    def get_name(self):
        return self._name

    # setter
    def set_name(self, name):
        self._name = name

    # 如果不用getter和setter可以用property函数
    name = property(get_name, set_name)


p = Person('tom')
p.name = 'Javier'
print(p.name)

print('Property装饰器'.center(30, '#'))


class Dog:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


d = Dog('huanhuan')
d.name = 'qiuqiu'
print(d.name)


class CLanguage:
    def set_name(self, name):
        if len(name) < 3:
            raise ValueError('must greater than 3')
        self.__name = name

    def get_name(self):
        return self.__name

    name = property(get_name, set_name)

    def set_add(self, add: str):
        if add.startswith('http://'):
            self.__add = add
        else:
            raise ValueError('must start with http://')

    def get_add(self):
        return self.__add

    add = property(get_add, set_add)

    def __display(self):
        print(self.__name, self.__add)


clang = CLanguage()
clang.name = "Python"
clang.add = "http://c.biancheng.net/view/2287.html"
print(clang.name, clang.add)
clang._CLanguage__display()
