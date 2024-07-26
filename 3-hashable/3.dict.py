'''
dict
Python 字典（dict）是一种无序的、可变，它的元素以key-value存储
相对地，列表（list）和元组（tuple）都是有序的序列，元素是顺序存放
每一个元素称为item，由key，value组成
虽然字典是一种无序的，但键值对在底层是有存储顺序
key是可hash类型，确保唯一，使用key来判断是效率最高的，时间复杂度是O(1)

字典查找
dict[key], key in dict，dict.get(key, default)，len(dict)
dict.setdefault(key, value), 如果key存在就返回，没有则赋值并返回value
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

在for循环遍历hash表结构的时候，不能改变字典长度

python3.6之前，字典是无序的，使用OrderedDict来表示有序字典
但是在python3.6之后，字典是按照录入顺序，相当于"有序"

如果要使用有序字典，要引入OrderedDict
'''

from collections import OrderedDict

print('字典构建'.center(30, '#'))
print(dict(), {})
# 标识符没有类型，会自动转成字符串类型
print(dict(a='a', b='b'))

# 也可以是二元组组成的顺序表对象
print(dict([('a', 1), ('b', 2), ('c', 3)]))

# 用zip函数创建
keys = ['one', 'two', 'three']
values = [1, 2, 3]
print(dict(zip(keys, values)))

print(dict({'a': 1, 'b': 2}, c=3, d=5, b=10))

# value指向同一个对象，最好不用
# print(dict.fromkeys('abc', [1]))


print('查找'.center(30, '#'))
d = {'a': 'apple', 'b': 'behind'}
# 如果没有找到，不会异常，可以指定返回内容，默认是None
print(d.get('X', 'NA'))
print('a' in d)

print('set default'.center(30, '#'))
print(d.setdefault('x', 'xv'))
print(d.setdefault('a', 'all'))
print(d)


print('更新'.center(30, '#'))
d.update({'c': 'catalina', 'd': 'divo'})
print(d)

print('删除'.center(30, '#'))
print(d.pop('a'))
del d['x']
print(d)
del d

print('遍历'.center(30, '#'))
scores = {'math': 95, 'physical': 85, 'chemistry': 75}
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

# 1. 集合和字典在以keys(), values(), items()遍历时不能修改字典的长度，但可以修改
# for k in scores:
#     scores.pop(k)

# 2. 如果用while循环则可以改变长度
# while len(scores):
#     scores.popitem()

# 3. 就想用for改变的话
keys = []
for k in scores:
    if scores[k] < 80:
        keys.append(k)
for k in keys:
    scores.pop(k)
print(scores)


print('OrderedDict'.center(30, '#'))
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
