'''

高阶函数
条件：函数作为参数传入，或者作为返回值返回函数地址

科里化



'''

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