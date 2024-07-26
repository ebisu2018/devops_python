'''
字符串是字面常量，定义了不可以修改，字符组成的不可变的有序序列（顺序表）
python中只有字符串类型

+， 字符串拼接生成1个新的字符串

str.split()，把字符串切开，返回一个列表，可以指定最大切割的数，默认按space
str.rsplit()，从右边开始切割，一般获取文件名用，返回列表
splitlines()，只切换行符
partition(), 返回的固定元素个数的三元组，只切一下，无论有没有切到
rpartition()，从右边切，只切1次返回三元组，获取文件名常用

replace()，替换字符，生成一个新的字符串

strip()，去除前后的空白，或者指定去除前后的字符集合

str.startswith(),判断是否在开头位置，返回bool
str.endswith(),判断是否在结尾位置，返回bool

str.upper(), 返回大写
str.lower()， 返回小写
str.capitalize()，返回首字母大写
str.isalpha，判断是否是字母
str.isdigit()，判断是否是数字
str.isidentifier(),判断是否是标识符


字符序列 -> 二进制字节序列叫编码 encode()
反之，解码 decode()
Python3中是Unicode编码，2个字节存储，GBK也是2个字节，但编码不同
用哪个编码就用哪个解码，否则会不匹配

Unicode内存中使用2个字节编码
网络传输或者序列化采用UTF-8编码， 1-6字节（汉字3个字节）
乱码本质是编码和解码不一致

字节序列是字节序列，就是字节组成的二进制序列，和编码无关
字符和编码有关，需要编码表转换成字符

需要类型，来解释字节序列的意义
一段字节序列是按照整型理解还是用字符串理解

bytes()是不可变的，存储的是二进制，展示给人用十进制
bytearray，是字节列表，是可变的

切片不改变类型，原来是什么类型，切片还是什么类型

'''

import datetime

# index(), count(), find(), len()
# find()如果没有找到子字符串则返回-1
# index()如果没有找到子字符串抛出ValueError

# 可以设置按方向查找，rindex(), rfind()
# 可以指定start和end的位置范围查找

print('查找'.center(30, '#'))
s = 'abcabcabc'
print(s.index('bc'))
print(s.find('av'))
print(s.find('abc', 3))
print(s.count('b'))
print(len(s))

print('built-in'.center(30, '#'))
# 用指定的间隔符来联合join的可迭代对象，join参数是可迭代对象（元素必须是字符串类型），返回新字符串
print('-'.join('xxxxx'))
print('*'.join(map(str, range(5))))

print('abcd'.split('b'))
print('a/b/c/d'.split('/'))

# 只切两个
x = '/'.join('abcd')
print(x.split('/', 2))

# 获取文件名
print('/home/user/file'.rsplit('/', 1))
print('/home/user/file'.partition('/'))
print('/home/user/file'.rpartition('/'))

print('a\nb\tc\rd      \ne    \n  \t f'.split())
# 切割\r\n
print('a\r\nb\tc\rd      \ne    \n  \t f'.splitlines())

print('a,b,c'.replace(',', '-'))
print('     abc  \n  '.strip())
print('\n\t   a\nbcasdd  \r\n  \t'.strip('\n\t'))

print('abc'.startswith('a'))
print('abc'.endswith('c'))


print('字符串格式化输出'.center(30, '#'))
print('%d %.1f %s' % (10, 1.2, 12))

print(float('10'))
print('%f' % 10)
print('%-3d' % 10) #左对齐，占3位

d = {'name': 'Darwin', 'age': 20}
print('%(name)s %(age)d' % d)
print(f'{d["name"]}, {d["age"]}')


# 格式化时间字符串！！！
d1 = datetime.datetime.now()
print(d1)
print('{:%Y %y %m %b %d %H %M %S}'.format(d1))

# 居中对齐，30位长度，内容在中间，用#填充，如果没有指定填充符则用空格
print('{:#^30}'.format('central'))
print(1, 'central'.center(30, '#'))
print(2, '{:#^30}'.format('central'))
print(3, '{:#^{}}'.format('central', 30))

print('字节序列'.center(30, '#'))
print('abc'.encode(), bytes())
# \x代表十六进制数
print('啊'.encode(), b'\xe5\x95\x8a'.decode())

# bytes初始化
print(bytes('xyz', 'utf-8'), bytes(b'abc'))

b = b'abc'
print(b[:2])
print(b[1])

x = tuple(range(10))
print(x[1:1])
