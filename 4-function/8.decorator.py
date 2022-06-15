'''

高阶函数
条件：函数作为参数传入，或者返回函数的地址

函数柯里化：
必须是嵌套函数，外部函数返回内部函数的地址，内部函数有外部函数的局部变量闭包
这样调用的时候就可以用fn(a)(b)方式调用，实际执行的就是内部函数

计算时间对象：datetime.datetime.now()
相减得到的是timedelta对象，调用total_seconds()得到总共相差多少秒

装饰器
1. 无参装饰器，只接受wrapped函数名
传递的参数是函数对象，返回的是wrapper的函数地址
实际调用的是wrapper函数，wrapper函数__closure__中有wrapped的引用
需要先定义好装饰器函数才能使用装饰器
语法：
@decorator
def wrapped():

等价于 wrapper = decorator(wrapped)，返回的decorator内部的函数地址wrapper
当调用wrapped()的时候，相当于decorator(wrapped)(参数)

2. 带参装饰器
@wraps(wrapped)
def wrapper(*args, **kwargs):

等价于 wrapper = decorator(wrapped)(wrapper)
wraps装饰器，用于wrapped的属性覆盖wrapper的属性，外面看起来就像是调用的wrapped

总结：无论带不带参数，decorator的名字后面的参数一定是def中定义的函数对象

'''


# 函数柯里化
def counter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base
    return inc


f = counter(10)
print(f())
print(f())


def add(a):
    def inc(b):
        return a + b
    return inc


print(add(4)(5))


def mul(a):
    def inc(b):
        def inc1(c):
            return a * b * c
        return inc1
    return inc


print(mul(2)(3)(4))


print('装饰器'.center(30, '#'))
import datetime


def add(a, b):
    return a + b


print('###############')


from functools import update_wrapper, wraps


# 装饰器B，参数写在内部函数中，外层函数只传递函数对象
def logger(wrapped):

    @wraps(wrapped)  # 等价于 wrapper = wraps(wrapped)(wrapper)
    def wrapper(*args, **kwargs):
        print('before', args, kwargs)
        ret = wrapped(*args, **kwargs) # 必须要解构，否则会变成元组和字典
        print('end')
        return ret

    # update_wrapper(wrapper, wrapped) # 使用包函数修改，一般不使用这个函数
    return wrapper


# 相当于add = logger(add)，本质add指向的是内部wrapper函数地址，wrapper函数有闭包，closure包含了wrapped函数的引用
@logger
def add(x, y):  # 把标识符作为logger的wrapped传入，覆盖此标识符
    return x + y


# 相当于调用wrapper函数，相当于logger(add)(10, 20)
print(add(10, 20))

