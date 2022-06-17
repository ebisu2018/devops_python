'''

函数，封装一段功能代码块来复用

def是表示定义函数的关键字
后面的是函数标识符，标识符指向函数对象
参数列表，定义函数是形式参数
内部是函数语句块
return是返回值，如果没有默认返回None

函数标识符由字母数字下划线组成，不能数字开头，不能和keyword重复
定义是定义，在堆内存中生成函数对象，是一堆指令
调用是调用，先定义才能调用，调用函数需要在标识符后面加括号，调用参数是实际参数，会在栈中开辟新空间来运行
函数是callable，可以使用callable(标识符)检验是否是可调用对象
函数参数不需要指定类型，因为python是动态类型的


传递 实参 的两种方式：
position参数，实参和定义形参的顺序一致
keyword参数，指定关键字，顺序任意指定，需要指定参数名，不用加引号
可以混合使用，但是位置参数必须在关键字参数之前


定义 形参 方式
1. 普通形参，可以指定默认值，可以使用位置或者关键字传递

2. 可变参数*args，用*args定义，必须传递位置参数
            不管有多少个参数，构成一个元组类型，如果没有给则是空元组
            必须在可变关键字之前
            函数中用*args解构

3. 可变关键字**kwargs，用**kwargs定义，必须用关键字方式传递参数！
                  关键字参数构成一个字典，如果没有则是空字典
                  一定放在参数最后
                  函数中用**kwargs解构
注：可变参数没有默认值！

4. keyword-only参数：出现在*args或者 * 之后，必须指定关键字，作为一种强调
                如果有默认值，无所谓顺序

5. position-only参数：参数出现在 / 之前，前面的参数是仅位置传入参数，不可以指定关键字！
python3.8之后才有的语法


场景：
iterable是仅位置参数，*不关心，后面的key和reverse是仅关键字参数!
sorted(iterable, /, *, key=None, reverse=False)

函数的定义，重要的参数列在外面，常改变的尽量前置，不常改变的后置


参数解构
*，可迭代对象需要解构传入进去，如果是字典取的是key
**，只能用于字典，按照key value的形式传参，相当于关键字传参

返回值
如果没有返回值，默认return或者return None
return之后的语句不会执行，中断函数执行
return看似可以返回多个值，本质封装在一个元组中

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
dic = {'x': 100, 'y': 200, 'z': 300}
add(**dic)


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


# 参数解构，传入字典
def fn(x, y):
    print(x, y)


# 两个*，传入的参数是字典，则是关键字传参！
fn(**{'x': 1, 'y': 2})  # 相当于fn(x=1, y=2)

# 一个*传入参数是字典，则获取的是key！
fn(*{'x': 1, 'y': 2})  # 相当于fn('x', 'y')
