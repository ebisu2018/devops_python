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
del, 删除对象

头部或者中间删除，后面数据向前移动，效率低，时间复杂度O(N)
尾部删除，其他数据不需移动，效率高，时间复杂度O(1)

改：
不会引起数据的移动，直接通过索引定位，效率很高，时间复杂度O(1)
通过索引修改直接覆盖

查：
通过索引查找，效率高，时间复杂度O(1)
len()方法查找，效率高，序列会记录来len，时间复杂的O(1)
index()和count()的时间复杂度是O(N)，因为需要遍历查找

list.reverse()是列表反转，会修改元列表，没有返回值，不建议使用
list.sort(), 对列表元素排序，修改元列表，没有返回值，不建议使用
reversed()内建函数，生成可迭代器对象，并不会修改元列表，效率高
sorted(), 内建函数，生成一个新的列表，默认升序，效率高

对象的创建，生命周期，垃圾回收，都是在内存的堆中

垃圾回收：核心是引用计数器，目的是整理碎片化内存，垃圾回收适当的时候触发
引用计数为0就是垃圾，虚拟机判断其为垃圾会在合适的时机清除
del删除了指定变量，且该变量所占用的内存再没有其他变量使用，此内存空间也不会真正地被系统回收并进行二次使用，它只是会被标记为无效内存
如果想让系统回收这些可用的内存，需要借助 gc 库中的 collect()函数
Python 自带垃圾回收功能，会自动销毁不用的对象，所以一般不需要通过 del 来手动删除

列表复制
list()创建的列表是生成一个全新对象
==，用来判断内容是否相等
is，用来判断内存引用是否相等

copy()，默认是浅拷贝，复制出一个新的对象，复制每个元素的地址
copy.deepcopy(), 深拷贝，如果元素是引用类型，会跟进去做递归副本
'''
import copy

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

print('append'.center(30, '#'))
language = ["Python", "Go", "Java"]
print(language)
language.append('PHP')
print(language)
language.append(('JavaScript', 'C#', 'Go'))
print(language)
language.append(['Ruby', 'SQL'])
print(language)

print('extend'.center(30, '#'))
language = ['Python', 'Go', 'Java']
language.extend('C')
print(language)
language.extend(('JavaScript', 'C#', 'Go'))
print(language)
language.extend(['Ruby', 'SQL'])
print(language)

print('insert'.center(30, '#'))
language = ['Python', 'Go', 'Java']
language.insert(-10000, 'C')
print(language)
language.insert(10000, ('Javascript', 'Typescript'))
print(language)
language.insert(3, ['Ruby', 'SQL'])
print(language)

print('remove'.center(30, '#'))
lang = ["Python", "Go", "Java", "Javascript"]
del lang[-1]
print(lang)
print(lang.pop(-1))
print(lang)
lang.remove("Go")
print(lang)
lang.clear()
print(lang)
del lang


print('search'.center(30, '#'))
print(language)
print(language.index('Java'))
print(language.count('Devops'))
print(len(language))

# 这种乘法生成的全新列表，其实内部是引用
a = [[1]] * 3
for i in a:
    print(id(i))
a[1][0] = 100
print(a)

print('内建函数'.center(30, '#'))
l = list(range(5))
print(l)
l.reverse()
print(l)

l.sort()
print(l)

print(reversed(l))
print(sorted(l))

a = list(range(5))
b = list(range(5))
print(a == b, a is b)
a[1] = 100
print(a == b, a is b)


print('Copy'.center(30, '#'))
a = list(range(5))
b = a.copy()
a[1] = 100
print(a == b, a is b)

a = [1, [2, 3], 4]
b = a.copy()
print(a, b)

a[1][1] = 10
print(a, b, a == b)

b = copy.deepcopy(a)
a[1][1] = 20
print(a == b, a, b)
