'''

高阶函数
条件：函数作为参数传入，或者返回函数地址

函数柯里化：
必须是嵌套函数，外部函数返回内部函数的地址，内部函数有闭包
这样调用的时候就可以用fn(a)(b)方式调用，实际执行的就是内部函数

计算时间对象：datetime.datetime.now()
相减得到的是timedelta对象，调用total_seconds()得到总共相差多少秒

装饰器
1. 无参装饰器，只接受一个wrapped函数名
传递的参数是函数对象，返回的是包装后wrapper的函数地址
实际调用的是wrapper函数，wrapper函数__closure__中有wrapped的引用
需要先定义好装饰器函数才能使用装饰器
语法：
@decorator
def wrapped():

等价于 wrapper = decorator(wrapped)，返回的decorator内部的函数地址wrapper
当调用wrapped()的时候，相当于decorator(wrapped)(参数)，即wrapper(参数)

2. 带参装饰器
wraps装饰器，用wrapped的属性覆盖wrapper的属性，外面看起来像是就是调用wrapped

@wraps(wrapped)
def wrapper(*args, **kwargs):
等价于 wrapper = wraps(wrapped)(wrapper)

解析：
def wraps(wrapped, assigned = WRAPPER_ASSIGNMENTS, updated = WRAPPER_UPDATES):
    return partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)
因为只接受一个函数作为参数，因此可以使用装饰器！
本质调用的是partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)，是一个偏函数对象！
再调用偏函数对象加上参数wrapper，相当于调用了update_wrapper(wrapper, wrapped)
wraps(wrapped) -> fn = partial(update_wrapper, wrapped=wrapped) -> fn(wrapper)

总结：无论带不带参数，decorator后面的参数一定是def中定义的函数对象

'''
from functools import update_wrapper, wraps


print('函数柯里化'.center(30, '#'))


def counter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base
    return inc


f = counter(10)
print(f.__name__, f.__closure__)
print(f())
print(f())


def add(a):
    def inc(b):
        nonlocal a
        a += b
        return a
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


def add(a, b):
    return a + b


# 无参装饰器，参数写在内部函数中，外层函数只传递函数对象
def logger(wrapped):

    @wraps(wrapped)  # 带参装饰器：这一行等价于 wrapper = wraps(wrapped)(wrapper)
    def wrapper(*args, **kwargs):
        print('before', args, kwargs)
        ret = wrapped(*args, **kwargs)  # 必须要解构，否则会变成元组和字典
        print('end')
        return ret
    # update_wrapper(wrapper, wrapped) # 可使用包函数修改，一般不使用这个函数
    return wrapper


# 装饰器标识符相当于add = logger(add)，本质add指向的是内部wrapper函数地址，wrapper函数有闭包，closure包含了wrapped函数的引用
@logger
def add(x, y):  # 把标识符作为logger的wrapped传入，覆盖此标识符
    return x + y


# 相当于调用wrapper函数，相当于logger(add)(10, 20)
print(add(10, 20))
print(add.__closure__, add.__name__)


print('Exercise'.center(30, '#'))


def china(wrapped):
    def wrapper(*args, **kwargs):
        print('包在国土范围之内')
        wrapped(*args, **kwargs)
        print('包在国土范围之内')
    return wrapper


@china
def taiwan(province: str):
    print(f'中国 {province}省')


taiwan('台湾')
print(taiwan.__closure__, taiwan.__name__)
