'''
格式化字符串
1. format字符串，大括号和值是一一对应，{}代表占位符，值写在format中
2. f前缀-插值字符串，python3.6之后才有，变量写在{}中

标识符
编译完没有标识符，标识符是给人看的，指向内存中一个地址
内存中是线性有序的，以地址来获取里面存储的值，需要标识符指向地址才可以
地址相当于门牌号码，里面住的人是值
规范：字母数字下划线组成，不能以数字开头
尽量都是小写，尽量不要下划线开头，大写开头的是定义类用，单词之间用下划线来间隔

标识符分为常量和变量
标识符可以被重新修改指向
常量是定义就不能修改标识符指向
python中没有标识符常量，任何标识符都可以修改指向
python中有字面常量，是不可变，值定义好了就不能改变

python是动态
动态：变量不需要声明类型，可以改变类型，赋值那一刻决定了类型，运行的时候才能发现错误，如python，js
静态：变量需要声明类型，不能随意改变类型，编译时检查类型错误，如java，c
***类型注解，只是提醒用的，但并不实际校验，非强制***

python是强类型语言
强类型：不同类型之间操作需要强制转换
弱类型：不同类型之间操作不需要强制转换

bool类型，bool()内建函数，是int的子类，可以参与计算，分为True和False
False有False，None，''，0，空容器([], {}, (), set())，其他为True

逻辑运算符/短路运算符 and or not，not会隐式转换成bool类型
计算运算符 %表示取余数，**表示幂
位运算符  << n 相当于乘以2的n次方，>> n 相当于除以2的n次方
比较运算符，除了数值类型，最好同类型比较，返回bool类型
成员运算符 in not in
身份运算符 is is not

type类是int str的元类

print默认用空格分割，末尾有回车，可以指定sep，end，file参数自定义输出
'''


import decimal
from fractions import Fraction

a = 100
b = 200
c = 'abc'

# 2种格式化字符串
print('{} + {} = {}'.format(a, b, (a + b)))
print(f'{a} + {c}')

# 换行
a = ("asdasdasdadsasda"
     "dasdasdasdasdasd")
print(a)

# 类型注解
a2: int = 10

print(1 > 1.2)

print(int('123'))
print(float('1.23'))
print(int("10"))
print(type(14e2))

print(type(a) == str)
# 类型判断推荐写法
print(isinstance(1, (bool, str, int)))
print(1, 2, 3, sep='\t', end='\n\n')

# 方便阅读用十进制输出
print(0x45, 0o26)

# 用进制格式输出
print(hex(99), bin(128), oct(10))
