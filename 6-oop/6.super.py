'''

在子类中的构造方法中，调用父类构造方法的方式有 2 种，分别是：
类可以看做一个独立空间，在类的外部调用其中的实例方法，可以向调用普通函数那样，只不过需要额外备注类名（此方式又称为未绑定方法）；
使用 super() 函数。但如果涉及多继承，该函数只能调用第一个直接父类的构造方法。

'''


class People:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("我是人，名字为：", self.name)


class Animal:
    def __init__(self, food):
        self.food = food

    def display(self):
        print("我是动物,我吃", self.food)


# People中的 name 属性和 say() 会遮蔽 Animal 类中的
class Person(People, Animal):
    def __init__(self, name, food):
        super().__init__(name)
        Animal.__init__(self, food)


p1 = Person('jim', 'banana')
p1.say()
p1.display()
