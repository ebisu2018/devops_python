'''

python是动态类型语言
类型出现问题时只有在运行的时候发现，因此危险，难理解阅读
建议在写时候加上类型注解！

annotation，类型注解，非强制性的
用于告诉阅读者该变量是什么类型返回值什么类型，不是强制类型语言，因此只是提示作用
IDE仅仅友好提醒，并不会报错

: 类型，代表变量的类型
-> 类型，代表返回值类型，链式编程的时候可以做自动补全

__annotation__，是一个字典，包含了参数以及返回值的类型注解
{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

inspect模块
调用inspect.signature(fn).parameters()，得到的是OrderedDict，key是变量名，值是Parameter对象
包含4个属性
变量名name, 变量默认值default, 变量类型注解annotation类型, 变量参数类型kind

'''

import inspect


# 设定变量类型和返回值类型
def add(a: int, b: int) -> int:
    return a + b


print(add(3, 5))

# 仅提示并不会报错
print(add('a', 'b'))

print(add.__annotations__)


# 设置变量的类型注解
a: list = []
b: dict = {}
c: str = 'abc'


# inspect模块
# 判断是否是函数
print(inspect.isfunction(add))

# 看函数签名
sig = inspect.signature(add)
print(sig)

# 获取参数，参数对象是一个OrderedDict
params = sig.parameters
print(params)  # OrderedDict([('a', <Parameter "a: int">), ('b', <Parameter "b: int">)])
print(params.keys())
print(params.values())
print(params.items())

for k, v in params.items():
    print(k, v, v.name, v.default, v.annotation, v.kind)


from functools import wraps


# 类型检查装饰器函数
# 相当于wrapped = check(wrapped)


def check(wrapped):
    @wraps(wrapped)
    def wrapper(*args, **kwargs):

        # params: OrderedDict([('a', <Parameter "a: int">), ('b', <Parameter "b: int">)])
        params = inspect.signature(wrapped).parameters
        for i, p in zip(args, params.values()):
            if p.annotation != p.empty and not isinstance(i, p.annotation):
                raise TypeError("{} = {} is False".format(p.name, i))

        for k, v in kwargs.items():
            if params[k].annotation != inspect._empty and not isinstance(v, params[k].annotation):
                raise TypeError("{} = {} is False".format(params[k].name, v))

        ret = wrapped(*args, **kwargs)
        return ret
    return wrapper


@check
def add(x: int, y: int):
    return x + y


print(add(5, 5))
# print(add('3', 7))
# print(add(2, y='8'))
