'''

闭包 closure
条件：出现在嵌套函数中，内层函数引用外层函数的自由变量，外层函数返回的是内层函数的地址！
内层函数引用外层函数定义的变量，那个变量也叫自由变量

每一次函数的执行是独立的，函数调用完后局部变量会被释放

闭包原理
定义函数只是在内存中开辟了一块空间来存放函数对象以及指令
当函数执行的时候会新开辟一块空间，并生成出局部变量和内部函数对象返回给标识符（内层函数并没有执行）
当返回的内层函数地址返回并被执行的时候，python闭包已经把外层的自由变量的引用保存放在__closure__中
即使外部函数的局部变量被释放，内部函数依然保留了外部函数的局部变量的引用！！
这就是为什么执行完inc返回inner后依然能找到外部函数变量的原理

nonlocal，指明变量不是本地的局部变量，也不是全局global变量，而是到某一级外层函数的局部变量
nonlocal不能引用全局global变量，因此必须出现在嵌套函数中！

嵌套函数加载局部变量作用域的机制
LEGB机制, local, enclosing, global, build-in
优先用local变量，没有则找外层函数作用域，没有则找global作用域，没有则找build-in，还没有则是NameError异常

'''


def inc():
    a = 100
    c = [0]  # 自由变量，执行完inc函数后会被释放，但是inner会引用此变量地址

    def inner():
        print(a)
        c[0] += 1
        return c[0]
    return inner


fn = inc()
print(fn.__name__)  # 查看函数的名字
print(fn.__closure__)  # 查看闭包，包含的对象地址
print(fn())
print(fn())

print('nonlocal'.center(30, '#'))

def inc():
    a = 0
    def inner():
        nonlocal a
        a += 1
        return a
    return inner

fn = inc()
print(fn())



