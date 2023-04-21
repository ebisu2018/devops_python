'''

作用域
就是名称空间，标识符的可见范围
限制在当前的作用域中，对外不可见

分为全局作用域和局部作用域
顶级标识符都是全局的，全局可见
函数或者类内部是局部的，只是局部可见

当函数被执行时，Python 会为其分配一块临时的存储空间，所有在函数内部定义的变量，都会存储在这块空间中
而在函数执行完毕后，这块临时存储空间随即会被释放并回收，该空间中存储的变量自然也就无法再被使用


全局的变量，向内穿透，函数可以看到外部的变量
函数内部的local变量，从外面无法访问，只是内部访问

如果局部变量和外层的变量重名，则内部局部变量优先级更高

global 关键字
如果函数中出现了和全局变量名一致的赋值语句，则认为它就是函数的局部变量，需要先赋值才可以引用！否则会报unbound的错误
在函数内部对不存在的变量赋值时，默认就是重新定义新的局部变量
如果想函数内部引用并修改全局变量，则用global关键字声明再修改!
在函数体内定义全局变量，使用 global 关键字对变量进行修饰后，该变量就会变为全局变量

nonlocal关键字
nonlocal，指明变量不是本地的局部变量，也不是全局global变量，而是到嵌套函数外层函数的局部变量
nonlocal不能引用全局global变量，因此必须出现在嵌套函数中！

嵌套函数加载局部变量作用域的机制
LEGB机制, local, enclosing, global, build-in
优先用local变量，没有则找外层函数作用域，没有则找global作用域，没有则找build-in，还没有则是NameError异常

globals()和locals()
通过调用 globals() 函数，我们可以得到一个包含所有全局变量的字典，key是变量名，value是变量值
并且，通过该字典，可以访问指定变量，还可修改它的值
locals() 返回的局部变量组成的字典，可以用来访问变量，但无法修改变量的值

总结：全局变量是公用的，一般情况不要修改，尽量使用局部变量

'''

print('使用全局'.center(30, '#'))
a = 10


def fn():
    print(a)


fn()


print('优先级'.center(30, '#'))


def outer():
    o = 65

    def inner():
        o = 97
        print('inner', o, chr(o))
    inner()
    print('outer', o, chr(o))


outer()


print('引用全局'.center(30, '#'))
z = 100


def fn():
    global z
    z += 10
    print(z)


fn()


print('函数内定义全局'.center(30, '#'))


def test():
    global web_url
    web_url = "https://www.python.org"
    print("函数体内访问：", web_url)
    # 此处定义的是全局变量，因此在locals中看不到此全局变量
    print(locals())


test()
print('函数体外访问：', web_url)


def inc():
    a = 0

    def inner():
        nonlocal a
        a += 1
        return a
    return inner


fn = inc()
print(fn())

print(globals())
# 作用相当于globals()
print(vars())
