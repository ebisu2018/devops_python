'''

函数，封装一段功能代码块来复用

def是表示定义函数的关键字
后面的是函数标识符，标识符指向函数对象，标识符指向的内容可以随便更改
参数列表，定义的是形式参数
内部是函数语句块
return是返回值，如果没有默认返回None

函数标识符由字母数字下划线组成，不能数字开头，不能和keyword重复
定义是定义，在内存中生成了函数对象，是一堆指令
调用是调用，先定义才能调用，调用函数需要在标识符后面加括号，调用参数是实际参数，会开辟新的空间来运行函数
函数是callable，可以使用callable(标识符)检验是否是可调用对象
函数参数不需要指定类型，因为python是动态类型的，注意传递的参数类型
调用函数用标识符加上括号就可以调用


传递 实参 的两种方式：
位置参数，实参和定义形参的顺序一致
关键字参数，指定关键字，和顺序无关，需要指定参数名！
可以混合使用，但是位置参数必须在关键字参数之前！


定义形参的方式
普通形参，可以有默认值，可以使用位置或者关键字传递

可变参数*args，用*定义，必须传递位置参数
            不管有多少个参数，构成一个元组类型，如果没有给则是空元组
            必须在可变关键字前

可变关键字**kwargs，用**定义，必须用关键字方式传递参数！
                  关键字参数构成一个字典，如果没有则是空字典
                  一定放在参数的最后

注：可变参数没有默认值！

keyword-only参数：出现在*args或者*之后，必须指定关键字，作为一种强调
                如果有默认值，无所谓顺序

position-only参数：参数出现在/之前，前面的参数是仅位置传入参数，python3.8之后


场景：
iterable是仅位置参数，*不关心，后面的key和reverse是仅关键字参数
sorted(iterable, /, *, key=None, reverse=False)

函数的定义，重要的参数列在外面，常改变的尽量前置，不常改变的后置


参数解构*，实参的可迭代对象需要解构传入进去，如果是字典取的是key
**，只能用于字典，按照key value的形式传参，相当于关键字传参

返回值
如果没有返回值，默认return或者return None
return之后的语句不会执行，中断函数的执行
return看似可以返回多个值，但是封装在一个元组中

'''

print('位置参数')
def add(a, b):
    print(a, b)
    return a + b

print(add(2, 4))
print(callable(add))


print('关键字参数')
print(add(b=3, a=5))

def login(host='local', port=3306, username='root', password='root'):
    conn_str = "mysql://{}:{}@{}:{}".format(username, password, host, port)
    print(conn_str)


login()
login('192.168.1.1', username='admin', password='admin')

print('可选形参')
def add(*args):
    print(type(args), args)

add()
# <class 'tuple'> (1, 2, 3, 4, 5)
add(1, 2, 3, 4, 5)
add(*range(5))


print('可变关键字形参')
def add(**kwargs):
    print(type(kwargs), kwargs)

add()
add(a=1, b=2, c=3)


def config(host, port=3306, **kwargs):
    print(host, port, kwargs)


config('localhost', a=1, b=2, c=3)


print('keyword-only')
def foo(*args, a, b):
    print(a, b, args)

foo(1, 2, a=3, b=4)


def foo(*, x, y):
    print(x, y)

foo(x=3, y=4)


def foo(a, b, /):
    print(a, b)

foo(2, 5)


# 汇总，一般不用写这么复杂
def fn(a, b, /, c, d=10, *args, m, n, **kwargs):
    print(a, b, c, d, args, m, n, kwargs)


fn(1, 2, 3, 5, m=12, n=34, x='kw')

def config(host, username='admin', password='admin', *, port=3306, **options):
    db = options.get('db', 'test')
    connstr = "mysql://{}:{}@{}:{}/{}".format(username, password, host, port, db)
    print(connstr)


config('localhost', 'root', 'root', port=33060, db='cmdb')


def fn(x, y):
    print(x + y)

fn(**{'x': 1, 'y': 2})