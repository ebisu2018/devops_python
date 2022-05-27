'''
字符串是字面常量，定义了不可以修改
字符组成的有序序列，是不可变的
python中没有字符类型，都是字符串类型

r前缀，去除转义字符含义
f前缀，字符串插值

因为是不可变的，只可以查

查找的方法：
index(), count(), find(), len()
要注意时间复杂度
find()和index()找到了子字符串都会返回索引位置
find()如果没有找到子字符串则返回-1，更安全
index()如果没有找到子字符串则会抛出valueError

可以设置按方向查找，rindex(), rfind()
可以指定start和end的位置范围查找

+， 字符串拼接生成1个新的字符串
str.join(iterable)，用指定的间隔符来联合join的可迭代对象，join的参数是可迭代对象，返回一个新的字符串
str.split()，用分隔符把字符串切开，返回一个列表，可以指定最大切割的数，默认按space切
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

'''

print(r'\t\n\r')
s1 = 'hello'
s2 = 'python'
print(f'{s1}, {s2}')

s = 'abcabcabc'
print(s.index('b'))
print(s.count('b'))
print(len(s))
print(s.find('a'))
print(s.rfind('a'))
print(s.rindex('b'))

print(s.find('x'))
# print(str.index('x'))

print('a' + 'b')

print('-'.join('xxxxxx'))

a = map(str, range(5))
print('*'.join(a))

print('abcd'.split('b'))
print('a/b/c/d'.split('/'))

# 只切第一个
x = '/'.join('abcd')
print(x.split('/', 2))

# 获取文件名
print('/home/user/file'.rsplit('/', 1))

print('a\nb\tc\rd      \ne    \n  \t f'.split())

print('/home/user/file'.partition('/'))
print('/home/user/file'.rpartition('/'))

print('a,b,c'.replace(',', '-'))

print('     abc  \n  '.strip())
print('\n\t   a\nbcasdd  \r\n  \t'.strip('\n\t'))

print('abc'.startswith('a'))
print('abc'.endswith('c'))

# 字符串格式化输出
print('%d %.1f %s' % (10, 1.2, 12))

print(float('10'))
print('%f' % 10)
print('%-3d' % 10) #左对齐，占3位

d = {'name': 'jose', 'age': 20}
print('%(name)s %(age)d' % d)
print(f'{d["name"]}, {d["age"]}')


# 格式化时间字符串！！！
import datetime
d1 = datetime.datetime.now()
print(d1)
print('{:%Y %y %m %b %d %H %M %S}'.format(d1))

# 居中对齐，30位长度，内容在中间，用#填充，如果没有指定填充符则用空格
print('{:#^30}'.format('central'))


# 字节序列
print('abc'.encode())
print('啊'.encode())

x = [[10], 10]
y = x[:]
print(id(x), id(y))

for i in x:
    print(id(i))

for i in y:
    print(id(i))
