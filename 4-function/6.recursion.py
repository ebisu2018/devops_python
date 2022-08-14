'''

递归函数

函数内部调用自己，需要有弹出条件，否则会栈溢出，内存泄漏
因为总要分配栈帧，执行每个函数，所以效率低
尽量使用普通的循环！避免使用递归函数

'''

# 普通版本


def fib1(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b


print(fib1(101))


# 递归版本
def fib2(n, a=1, b=1):
    if n < 3:
        return b
    a, b = b, a + b
    return fib2(n - 1, a, b)


print(fib2(3))
print(fib2(5))
