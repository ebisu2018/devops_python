'''

类中的方法：

1. 普通方法（self）
类中的大多数方法都是有self参数的，通过实例调用方法
实例.方法 等同于 类.方法(实例)
方法绑定：当用实例.方法调用的时候，实例会和方法绑定，作为第一个参数传递给self
非绑定：类.方法(实例)，需要手动把实例传给self！

2. @classmethod 装饰器 本质fn = classmethod(fn)
参数是cls，用类或者实例都可以调用classmethod，但是推荐用类调用类方法
不管是类或者实例调用类方法，参数cls一定都是类！因为实例通过实例.__class__访问到类
因此 类 会作为第一个参数绑定到类方法中！

3. @staticmethod，没有方法绑定，不需要传递类或者实例！
可以通过类或实例调用静态方法

'''


class A:

    def fn(self):
        print(f'I am {self}')


i = A()
i.fn()
# 等同于
A.fn(i)


class A:
    @classmethod
    def fn(cls):
        print('class method', cls)


a = A()
print(A.__dict__)
A.fn()
a.fn()


class A:
    @staticmethod
    def fn():
        print('static method')


a = A()
A.fn()
a.fn()
