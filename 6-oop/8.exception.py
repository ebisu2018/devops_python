'''

try不能单独使用，要和其他关键字一起使用
遇到异常后，后面的代码不会执行，直接进入到except中
处理异常完，后面的代码依然会执行

Raise
不能单独使用，必须接异常类或者异常实例！
可以自己附加描述信息，如果没有描述信息则是空
raise *Error
raise *Error()
raise *Error(msg)
错误信息可以在exception的 e 中捕获
str(e)是错误字符串, e.args()是一个元组

所有异常的父类都是BaseException
BaseException的结构:
1. SystemExit
2. KeyboardInterrupt
3. GerneratorExit
4. Exception，下面有若干子类

自定义异常一般继承Exception即可
类内部什么都不用写

多个Exception的原则：
多个Exception是先子类后父类！缺省Exception写在最后
Exception中可以捕获所有的exception的子类异常。要注意顺序

finally一定在最后，可以和try一起使用，也可以和try except一起使用
不管有没有异常，最终finally一定执行，比如文件的关闭
函数中如果finally中又return，则会压制住异常，一般不使用

else关键字
如果代码没有异常，则会执行else子句
如果有Except，则不会执行else子句

一般结构
try: 运行代码块
except: 异常捕获执行
else: 没有异常则执行
finally: 总会执行

不能把所有的异常都处理，适当的时候需要抛出异常

'''

# raise
try:
    raise IndexError('index error')
except IndexError as e:
    print(e, str(e), type(e), e.args)


try:
    # 1/0
    raise TypeError('Type Error!!!')
except TypeError as e:
    print(e)
except IndexError as e:
    print(e)
except KeyboardInterrupt:
    print('Keyboard Error')
except Exception as e:
    print('except')
finally:
    print('finally')


print('=' * 30)


print('自定义异常'.center(30, '#'))
class MyException(Exception):
    pass


try:
    raise MyException('My Exception')
except MyException as e:
    print(e)


print('else'.center(30, '#'))
try:
    print('try')
except Exception as e:
    print(e)
else:
    print('else')
