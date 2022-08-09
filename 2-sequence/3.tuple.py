'''

元组
有序只读的，内容不可变
构造方法
tuple(), tuple(iterable), ()
只可以用index查询
+的拼接操作会生成一个新元组对象

一个空元组占了24字节

从内存上比列表效率更高，源码做了优化
占用小的会放到缓存中，之后就不用反复创建了

'''

# 构建
t = tuple()
print(t)

print((1,))

# 逗号分割的默认是元组类型
a = 1, 2
print(a)

# 将字符串转换成元组
tup1 = tuple("hello")
print(tup1)

# 将列表转换成元组
list1 = ['Python', 'Java', 'C++', 'JavaScript']
tup2 = tuple(list1)
print(tup2)

# 将字典转换成元组
dict1 = {'a': 100, 'b': 42, 'c': 9}
tup3 = tuple(dict1)
print(tup3)

# 将区间转换成元组
range1 = range(1, 6)
tup4 = tuple(range1)
print(tup4)

# 创建空元组
print(tuple())

print(t.__sizeof__())