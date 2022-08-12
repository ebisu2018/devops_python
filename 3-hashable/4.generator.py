'''

解析式和生成器表达式

解析式会构建一个新的列表或集合或字典
速度快，放在同一行中
只能有if，不能有else表达式

在中括号中是列表解析式
在大括号中是字典解析式或者集合解析式
在小括号中是生成器表达式！
使用元组推导式生成的结果并不是一个元组，而是一个生成器对象

生成器表达式：
(表达式 for 迭代变量 in 可迭代对象 [if 条件表达式] )
在小括号中构建的解析式，生成出来的是是生成器对象：generator！返回的是obj，内存地址


！！！！迭代器特点！！！！
1.只迭代一次，有指针，指针不回头
2.是惰性的，需要调用generator.__next__()计算
3.for循环可以迭代，如果到尽头，相当于迭代空容器不会异常；但是如果到尽头还调用__next__，则会抛出stopIteration异常
4.迭代器没有索引，因为可能有无限个元素！但是列表必须是有明确的长度边界！

迭代器：generator
可迭代对象：list，dict，tuple，set，string，range，其中range也是惰性，但是不是迭代器因为有索引并且可以重复迭代

列表会在内存中立刻构建，元素都预先生成出来，占用空间，但是获取元素快
生成器对象立即生成，但什么元素都没有，内存中只占用了生成器对象大小，调用__next__时才构建元素然后返回，节省空间，但是需要计算再返回
使用哪个取决于是否能容忍计算的时长


reversed(seq)，返回的是迭代器，逆序迭代器
sorted(iterable, key=None, reverse=False)函数返回一个有序列表
iterable 表示指定的序列，key 参数可以自定义排序规则；reverse 参数指定以升序（False，默认）还是降序（True）进行排序。sorted()


'''

print('列表解析式'.center(30, '#'))

a = [i ** 2 for i in range(5)]
print(a)

b = [i ** 2 for i in range(5) if i % 2]
print(b)

print([(i, j) for i in range(5) for j in range(3)])

src_a = [30, 12, 66, 34, 39, 78, 36, 57, 121]
src_b = [3, 5, 7, 11]
result = [(x, y) for x in src_b for y in src_a if y % x == 0]
print(result)


print('集合解析式'.center(30, '#'))
print({i * 2 for i in range(5)})


print('字典解析式'.center(30, '#'))
print({i: j for i in 'abc' for j in range(3)})
listdemo = ['wangyi', 'others']
new_dict = {k: len(k) for k in listdemo}
print(new_dict)


print('生成器表达式'.center(30, '#'))

a = (x for x in range(1, 5))
print(a)

print(a.__next__())
print(a.__next__())

# for i in a:
#     print(i, end='')
# print()

# 只能遍历一次！
print(tuple(a))


print('其他内建函数'.center(30, '#'))

print([str(i) for i in range(5)])
m = map(str, range(5))
print(m)

f = filter(lambda x: x > 5, range(1, 10))
print(f, list(f))

print(sorted((i for i in range(5))))
print(sorted(dict(a=1, b=2)))
print(sorted(dict(a=1, b='2').values(), reverse=True, key=str))

sites = ['http://c.biancheng.net',
       'http://c.biancheng.net/python/',
       'http://c.biancheng.net/shell/',
       'http://c.biancheng.net/java/',
       'http://c.biancheng.net/golang/']

print(sorted(sites, key=lambda x: len(x)))

my_list = [11, 12, 13]
my_tuple = (21, 22, 23)
z = zip(my_list, my_tuple)
print([i for i in z])
