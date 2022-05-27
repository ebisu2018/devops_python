'''

线性表
是一组元素的序列的抽象
分为顺序表和链表

顺序表：物理内存中开辟一段连续有序的空间，首地址已经分配固定，用index来表示索引，每个元素占用4字节
链表:
内存中没有顺序存放，但是依然有index，还是有序序列
链表自己记录了head地址，tail地址，和前一个以及后一个的地址

栈，属于LIFO，后进先出
队列，分为FIFO，先进先出；LIFO，后进先出；优先队列

时间复杂度是效率考量标准，O(1)表示固定的，随着N增大时间依然不变，O(N)表示随着N的增大，耗时增加

增：
在头部增加，引起后面数据的移动，效率低，时间复杂度O(N)
在中间插入，引起后面数据的移动，效率低，时间复杂度O(N)
在尾部追加，前面数据不需要移动，效率高，时间复杂度O(1)
append(obj) -> None, insert(index, obj) -> None
extend(list) -> None，+和*都是运算符重载是生成一个新的对象

删：
头部或者中间删除，后面数据向前移动，效率低，时间复杂度O(N)
尾部删除，其他数据不需移动，效率高，时间复杂度O(1)
remove(obj)没有返回值, pop(index)弹出并返回
clear(), 清空列表
del(), 删除引用

改：
不会引起数据的移动，直接通过索引定位，效率很高，时间复杂度O(1)
通过索引修改

list.reverse()是列表反转，会修改元列表，没有返回值，不建议使用
list.sort(), 对列表元素排序，修改元列表，没有返回值，不建议使用
reversed()内建函数，生成可迭代器对象，并不会修改元列表，效率高
sorted(), 内建函数，生成一个新的列表，默认升序，效率高

查：
通过索引查找，效率高，时间复杂度O(1)
注：index()和count()的时间复杂度是O(N)，因为需要遍历查找，尽量少用

垃圾回收：核心是引用计数器，目的是整理碎片化内存，垃圾回收适当的时候触发

列表复制
list()创建的列表是生成一个全新的对象
==，用来判断内容是否相等
is，用来判断内存引用是否相等

copy()，默认是浅拷贝，复制出一个新的对象，复制每个元素的地址
copy.deepcopy(), 深拷贝，如果元素是引用类型，会跟进去做递归副本

'''

# 创建空列表
l1 = list()
l2 = []

# 定义列表，传入可迭代对象
l3 = list(range(5))
l4 = list(['a', 'xyz', True, None, [1, 2, 3]])

# 获取列表长度
print(len(l4))

# 查询
print(l4.index('a'))
print(l4.count('a'))
print(len(l4))

# 增加
l4.append(100)
l4.insert(-1, 'q')
print(l4)
l3.extend(l4)
print(l3)

# 删除
l4.remove('a')

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