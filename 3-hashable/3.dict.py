'''

dict，字典，mapping
每一个元素称为item，由key和value组成的二元组
字典是可变，无序，key不重复的键值对数据类型

key是可hash类型，确保唯一，同时查找效率很高
字典使用key来判断是效率最高的，时间复杂度是O(n)

字典查找
dict[key], key in dict，dict.get(key, default)，len(dict)

dict.setdefault(key, value), 如果key有就返回值，没有则更新并返回值
如果不指定默认值则返回None

删除
del dict/dict['key']，可以删除字典或者里面的item
dict.pop(key)，弹出item并返回，需要指定key
dict.clear(), 清空字典内容

更新字典
dict.update()，更新字典，和构造类似，可以指定可迭代对象或者关键字参数

遍历字典其实遍历的就是key
可以指定keys(), values(), items()

！！！！和集合一样，字典在以keys, values, items遍历时不能修改字典的长度，但是可以修改value

幂等性：无论做多少次操作，结果都是一样
解释器如果不关闭，每次计算的hash值一定是一样的

python3.6之前，字典是无序的，使用OrderedDict来表示有序字典
但是在python3.6之后，字典是按照录入的顺序，相当于"有序"

如果要使用有序字典，要引入OrderedDict!!真正的有序字典，也是录入的顺序
使用方法和Dict一样
如果要保证顺序，建议使用OrderedDict！！

'''

from collections import OrderedDict


# 构造空字典
d1 = {}
d2 = dict()
print(d1, d2, dict([]), dict({}), dict(()))


# 构造带元素的字典，必须是在可迭代对象中，每个元素是二元组代表kv结构
d3 = dict([('a', 1), ['b', 2]])
print(d3)

# 标识符没有类型，会自动转成字符串类型！
d4 = dict(a=10, b=5)
print(d4)

d5 = dict({'a': 1, 'b': 2}, c=3, d=5, b=10)
print(d5)

# value指向同一个对象，不要用这个
print(dict.fromkeys('abcdef', [1]))

# 如果没有不会异常，可以指定返回内容，默认是None
print(d5.get('x', 'NA'))

print(d5.setdefault('x', 100))
print(d5.setdefault('a', 20))
print(d5)


print(d5.pop('a'))
print(d5)

for k in d5:
    print(k, d5[k])


for k in d5.keys():
    print(k)

for v in d5.values():
    print(v)

for item in d5.items():
    print(item)

for k, v in d5.items():
    print(k, v)