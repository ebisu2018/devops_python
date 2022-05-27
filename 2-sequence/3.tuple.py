'''
元组
有序只读的，内容不可变的
构造方法
tuple(), tuple(iterable), ()
只可以用index查询

从内存上比列表效率更高，源码做了优化

'''

# 构建
t = tuple()
print(t)

t = tuple(range(5))
print(t)

print((1,))

# 逗号分割的默认是元组类型
a = 1, 2
print(a)

