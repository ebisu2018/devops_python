'''
列表的常用操作

创建
1. 可以用[]的方式
2. 可以用list()方式，参数必须是可迭代对象
如果参数是字典，则通过key创建一个列表

增：
用+号对列表拼接，会生成一个新的列表
append(obj)，元素作为一个整体追加到列表中，列表原地修改无返回值
extend(obj)，元素逐个的添加到列表中，列表原地修改无返回值
insert(index, obj)，元素作为一个整体追加到列表中，列表原地修改无返回值

在头部增加，引起后面数据的移动，效率低，时间复杂度O(N)
在中间插入，引起后面数据的移动，效率低，时间复杂度O(N)
在尾部追加，前面数据不需要移动，效率高，时间复杂度O(1)


删：
remove(obj)没有返回值，指定元素删除，必须确保有元素
pop(index)弹出并返回
clear(), 清空列表
del, 删除某个元素或整个引用

头部或者中间删除，后面数据向前移动，效率低，时间复杂度O(N)
尾部删除，其他数据不需移动，效率高，时间复杂度O(1)


改：
不会引起数据的移动，直接通过索引定位，效率很高，时间复杂度O(1)
通过索引修改


查：
通过索引查找，效率高，时间复杂度O(1)
len()方法查找，效率高，序列会记录来len，时间复杂的O(1)
index()和count()的时间复杂度是O(N)，因为需要遍历查找，尽量少用


list.reverse()是列表反转，会修改元列表，没有返回值，不建议使用
list.sort(), 对列表元素排序，修改元列表，没有返回值，不建议使用
reversed()内建函数，生成可迭代器对象，并不会修改元列表，效率高
sorted(), 内建函数，生成一个新的列表，默认升序，效率高

垃圾回收：核心是引用计数器，目的是整理碎片化内存，垃圾回收适当的时候触发
del删除了指定变量，且该变量所占用的内存再没有其他变量使用，此内存空间也不会真正地被系统回收并进行二次使用，它只是会被标记为无效内存
如果想让系统回收这些可用的内存，需要借助 gc 库中的 collect()函数

列表复制
list()创建的列表是生成一个全新对象
==，用来判断内容是否相等
is，用来判断内存引用是否相等

copy()，默认是浅拷贝，复制出一个新的对象，复制每个元素的地址
copy.deepcopy(), 深拷贝，如果元素是引用类型，会跟进去做递归副本

'''

print('列表的创建'.center(30, '#'))
l1 = list()
l2 = []
l3 = list(range(5))
l4 = list(['a', 'xyz', True, None, [1, 2, 3]])
l5 = list({'a': 100, 'b': 'b', 'c': 200})
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)


print('增加'.center(30, '#'))
language = ["Python", "C++", "Java"]
birthday = [1991, 1998, 1995]
info = language + birthday
print("language =", language, id(language))
print("birthday =", birthday, id(birthday))
print("info =", info, id(info))

print('append'.center(30, '#'))
language.append('PHP')
print(language)
language.append(('JavaScript', 'C#', 'Go'))
print(language)
language.append(['Ruby', 'SQL'])
print(language)


print('extend'.center(30, '#'))
language = ['Python', 'C++', 'Java']
language.extend('C')
print(language)
language.extend(('JavaScript', 'C#', 'Go'))
print(language)
language.extend(['Ruby', 'SQL'])
print(language)


print('insert'.center(30, '#'))
language = ['Python', 'C++', 'Java']
language.insert(1, 'C')
print(language)
language.insert(2, ('C#', 'Go'))
print(language)
language.insert(3, ['Ruby', 'SQL'])
print(language)


print('删除'.center(30, '#'))
lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
del lang[1]
print(lang)
lang.pop()
print(lang)
lang.remove("Ruby")
print(lang)
lang.clear()
print(lang)
del lang


print('查找'.center(30, '#'))
print(language)
print(language.index('Java'))
print(language.count('Devops'))
print(len(language))

a = [[1]] * 3
for i in a:
    print(id(i))
a[1][0] = 100
print(a)


l = list(range(5))
print(l)
l.reverse()
print(l)

print(reversed(l))

l.sort()
print(l)

print(sorted(l))

a = list(range(5))
b = list(range(5))
print(a == b, a is b)
a[1] = 100
print(a == b, a is b)


a = list(range(5))
b = a.copy()
a[1] = 100
print(a == b, a is b)

a = [1, [2, 3], 4]
b = a.copy()
print(a, b)

a[1][1] = 10
print(a, b, a == b)

import copy
b = copy.deepcopy(a)
a[1][1] = 20
print(a == b, a, b)