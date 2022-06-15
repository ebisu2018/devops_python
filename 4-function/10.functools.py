'''

reduce(),将多个数据变成1个数据进行处理
有消减过程，例如阶乘
第一个参数与第二个参数计算得到的数字再作为第一个参数，继续接下去和第三个参数计算，以此类推

partial()，在函数式编程中常用，对传入的参数固定，返回一个包装函数
之后调用新函数的时候仅仅需要传入未固定的参数即可
被固定的参数无法被修改，如果是默认值参数被固定可以修改

partial()，本质是返回一个函数，类型装饰器一样
然后再调用返回的函数，可以参考柯里化或者装饰器的logger部分
partial(a)(b)

'''

from functools import partial, reduce, lru_cache
import inspect

def fn(a, b):
    print(a, b)
    return a + b


red = reduce(fn, range(5))
print(red)

red = reduce(lambda x, y: x * y, range(1, 6))
print(red)


print('Partial'.center(30, '#'))
def add(a, b=5):
    return a + b


# 相当于把6和add函数固定住了
newfn = partial(add, 6)
print(newfn, newfn())
# 传入的3会与固定的6相加！
print(newfn(3))

# 签名看仍旧只有一个默认值，看不到固定的参数值
print(inspect.signature(newfn))

newfn = partial(add, b=10)
print(inspect.signature(newfn))
print(newfn(10))

print({**{'a': 1}, **{'b': 100}})
