'''

正则表达式

基本的
. 匹配除了换行符之外的任意一个字符
[0-9] 匹配0-9中任何一个数字
[a-z]  匹配a-z的一个字符
[^a-z]  匹配除了a-z以外的一个字符
\d  匹配一个数字
\D  匹配除了数字以外的字符
\s  匹配任意一个空白
\S  匹配除了空白以外的字符
\w  匹配[a-zA-Z0-9]任意一个字符
\W  匹配除了[a-zA-Z0-9]以外任意一个字符
\b  匹配字符边界
^  不在中括号中表示以某个开头，必须是行首！
$  以谁结尾，必须是行尾！


重复
不可以单独使用，必须和基本的一起使用
* 任意个包括0个，等同于{0,}
+ 至少一个，等同于{1,}
？0或者1个，等同于{0, 1}
{m1, n} m到n个
{m1} 只出现m次

\d{11}, 匹配手机号码
\d{3, 4}-\d{7, 8}，匹配座机

或
（x | y）

分组 ()
如果正则中有小括号则会有分组，方便的拿出来使用
有几个小括号几个group，group0是match匹配的内容
(pattern) \n，将前面的分组重复引用n次

断言，此时小括号不是分组，断言成了才会匹配上，否则匹配不上
匹配上的不会输出！
(?=exp)，后面要出现，但是不会取得小括号中内容
(?<=exp)，左边要出现，但是不会取得小括号中内容
(?!exp)，右边不会出现的表达式
(?<tag>exp)， 带标签的匹配，可以通过字典获取

默认贪婪匹配，一般有.才会有的
在重复的符号后面加？就是不贪婪匹配
一般有 .*的时候才会造成贪婪


虽然文本是有换行的，但是在计算机看来依然是一行，只不过加上了\n
单行模式dot all，即使是多行，依然一行看待，因此\n对.照样可以穿透！
普通模式就是整体看成是一个字符串，不能匹配换行符
多行模式是有\n为换行符的多行文本，会影响^和$

多行模式
re.M
re.MULTILINE

单行模式
re.S
re.DOTALL

忽律大小写
re.I
re.IGNORECASE

忽略空白字符
re.VERBOSE

re.match()，必须从字符串索引0开始匹配或者指定区间匹配，如果没有找到则返回None
re.search()，在字符串内搜索，不一定是从头开始的，也可以指定区间
一定要注意单行模式还是多行模式， search出来的是match对象，group[0]是match出来的内容
fullmatch()，必须全部匹配，如果指定子串则要全部匹配

全文
findall()，在文本中全文搜索，返回的是一个列表，里面是匹配到的内容是字符串
finditer()，全文搜素，返回迭代器，元素是match对象， 通过索引0来获取value

re.sub，是对正则表达式匹配的内容进行替换，返回字符串

groups
如果正则表达式有小括号，则会对其进行分组，几个小括号几个元素，在一个元组中
如果只有一个分组则返回的是字符串

re.split('[pattern]')，切割用的
字符串的split方法其实就是\s+，尽可能的切割空字符串

'''


import re

s = '''bottle\nbag\nbig\napple'''
print('match')
m = re.match('b', s)
print(m)

# match是从头匹配，没有找到则返回None
regex = re.compile('^a', re.M)
m = regex.match(s)
print(m)

# 指定区间而不是从头match就可以找到
regex = re.compile('big', re.M)
m = regex.match(s, 11)
print(m)

print('search')
# 在字符串中搜索
m = re.search('^a', s, re.M)
print(m)

# 全部match
m = re.fullmatch('^b', s, re.M)
print(m)

# 必须全部匹配才可以
m = re.compile('bottle', re.M)
regex = m.fullmatch(s, 0, 6)
print(regex)

m = re.findall('^b\w+', s, re.M)
print(m)


x = re.sub('b\w', 'XXX', s)
print(type(x), x)

# 不常用
x = re.subn('b\w', 'XXX', s)
print(type(x), x)

print('Group'.center(30, '#'))
m = re.search('(b\w+)', s)
print(m, m.groups(), m[0], m.group(0))


m = re.search('(b)(\w+)', s)
print(m, m.groups(), m.group(0), m.group(1), m.group(2))

reg = re.compile('(b\w+)\n(b\w+)\n(b\w+)')
m = reg.findall(s)
print(m)
m = reg.search(s)
print(m.groups())
print(m)
print(m.group(0))

print('split')
s = '''os.path.abspath(path)\t\t\ngood'''
r = re.split('[.(),\s]+', s)
print(r)
