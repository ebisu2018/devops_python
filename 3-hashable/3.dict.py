'''

dict
Python 字典（dict）是一种无序的、可变的序列，它的元素以“键值对（key-value）”的形式存储
相对地，列表（list）和元组（tuple）都是有序的序列，它们的元素在底层是挨着存放的
每一个元素称为item，由key和value组成的二元组
虽然字典是一种无序的，但键值对在底层是有存储顺序

key是可hash类型，确保唯一，同时查找效率很高
字典使用key来判断是效率最高的，时间复杂度是O(1)

字典查找
dict[key], key in dict，dict.get(key, default)，len(dict)
dict.setdefault(key, value), 如果key存在就返回，没有则更新字典并返回value
如果不指定value则返回None

删除
del dict/dict['key']，可以删除字典或者里面的item
dict.pop(key)，弹出item并返回，需要指定key！
dict.popitem()，弹出最后一个item，不用指定key！
dict.clear(), 清空字典内容

更新字典
dict.update()，更新字典
在执行 update() 方法时，如果被更新的字典中己包含对应的键值对，那么原 value 会被覆盖
如果被更新的字典中不包含对应的键值对，则该键值对被添加进去
dict.setdefault(key, value), 如果key有就返回值，没有则更新后并返回
如果不指定默认值则返回None

字典的copy
遵循的是浅拷贝原则，copy() 方法只会对最表层的键值对进行深拷贝

!!!!集合和字典在以keys, values, items遍历时不能修改字典的长度，但是可以修改value!!!!

幂等性：无论做多少次操作，结果都是一样
解释器如果不关闭，每次计算的hash值一定是一样的

python3.6之前，字典是无序的，使用OrderedDict来表示有序字典
但是在python3.6之后，字典是按照录入顺序，相当于"有序"

如果要使用有序字典，要引入OrderedDict!!真正的有序字典，也是录入的顺序
使用方法和dict一样
如果要保证顺序，建议使用OrderedDict！！

'''

from collections import OrderedDict
print('创建字典'.center(30, '#'))
print({}, dict(), dict([]), dict({}), dict(()))

# 方式1
demo = [('two', 2), ('one', 1), ('three', 3)]
# 方式2
demo1 = [['two', 2], ['one', 1], ['three', 3]]
# 方式3
demo2 = (('two', 2), ('one', 1), ('three', 3))
# 方式4
demo3 = (['two', 2], ['one', 1], ['three', 3])
a = dict(demo)
print(a)

# 标识符没有类型，会自动转成字符串类型！
d = dict(a='a', b='b')
print(d)

# 用zip函数创建
keys = ['one', 'two', 'three']
values = [1, 2, 3]
d1 = dict(zip(keys, values))
print(d1)

d2 = dict({'a': 1, 'b': 2}, c=3, d=5, b=10)
print(d2)

# value指向同一个对象，最好不用
print(dict.fromkeys('abc', [1]))


print('查找'.center(30, '#'))
# 如果没有找到，不会异常，可以指定返回内容，默认是None
print(d2.get('X', 'NA'))
print('a' in d)

print('set default'.center(30, '#'))
print(d.setdefault('x', 10))
print(d.setdefault('a', 10))
print(d)

print('删除'.center(30, '#'))
print(d.pop('a'))
del d['x']
print(d)
del d

print('遍历'.center(30, '#'))
scores = {'数学': 95, '语文': 89, '英语': 90}
print(scores.keys())
print(scores.values())
print(scores.items())

for k in scores:
    print(k, scores[k])

for k in scores.keys():
    print(k)

for v in scores.values():
    print(v)

for item in scores.items():
    print(item)

for k, v in scores.items():
    print(k, v)

# 根据字典对格式化字符串
course = {'name': 'Python教程', 'price': 9.9, 'url': 'https://python.org'}
print(f"{course['name']} is {course['price']}, from {course['url']}")
print("{} is {} via {}".format(course['name'], course['price'], course['url']))


print('OrderedDict'.center(30, '#'))

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

for k, v in od.items():
    print(k, v)
