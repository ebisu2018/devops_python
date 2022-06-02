'''

解析式和生成器表达式

解析式会构建一个新的列表或集合或字典
速度快，放在同一行中
只能有if，不能有else表达式

在中括号中是列表解析式
在大括号中是字典解析式或者集合解析式
在小括号中是生成器表达式！

生成器表达式：
在小括号中构建的解析式，生成出来的是是生成器对象：generator！返回的是obj，内存地址
也是一个可迭代对象，但是只能迭代一次

列表和生成器都是可迭代对象

！！！！迭代器特点！！！！！
1.只迭代一次，有指针的东西，不会回头
2.是惰性的，需要调用next(generator)计算元素
3.for循环可以迭代，如果到尽头，相当于迭代空容器不会异常；但是如果到尽头还调用next()，则会抛出stopIteration异常
4.迭代器没有索引，因为可能有无限个元素！但是列表必须是有明确的长度边界！

迭代器有：generator
可迭代对象：list，dict，tuple，set，string，range，其中range也是惰性，但是不是迭代器因为有索引并且可以重复迭代

列表会在内存中立刻构建，元素都预先生成出来，占用空间，但是获取元素快
生成器对象立即生成，但什么元素都没有，内存中只占用了生成器对象大小，调用next()时才构建元素然后返回，节省空间，但是需要计算再返回
使用哪个取决于是否能容忍计算的时长

如果参数是生成器，则生成器表达式的小括号可以省略！

sorted()函数返回一个新的有序列表，参数是可迭代对象，所以包含生成器对象
可以指定reverse参数是否倒序排列，可以指定key来自定义函数对各个元素进行操作

'''

a = [i ** 2 for i in range(5)]
print(a)

b = [i ** 2 for i in range(5) if i % 2]
print(b)

print([(i, j) for i in range(5) for j in range(3)])

# 集合解析式
print({i * 2 for i in range(5)})

# 和map函数一样理解一样
print([str(i) for i in range(5)])

print(list(map(str, range(5))))

print(ord('x'), chr(0x61), bin(10), hex(20), oct(10))

# 字典解析式
print({i: j for i in 'abc' for j in range(3)})

x = (i+1 for i in range(5))
print(x)

for i in x:
    print(i)

# print(next(x))

print(sorted((i for i in range(5))))

print(sorted(dict(a=1, b=2)))

print(sorted(dict(a=1, b='2').values(), reverse=True, key=str))
