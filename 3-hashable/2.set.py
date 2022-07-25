'''

属于hash类型，key value结构，适用于做缓存系统
set集合，可变，无序，不重复的数据结构
自动去重
无序的，没有索引因此不能切片

set()，创建空集合
set(iterable)，参数是可迭代对象

!!!!!!!set中只能是可hash的对象!!!!!!
可变类型是不可hash
列表，集合，字典都是可变的，属于不可hash类型

集合可以增删改查
增
add()，把一个元素直接添加到集合中
update()，把可迭代对象中元素一一增加到集合中

删除
remove()，如果没找到则KeyError
discard()，有则删除没有也不会报错
clear()，清空集合
pop()，弹出任意一个

没有改，只能先删除再新增一个

查
in 成员标识符，判断是否在集合中

效率
hash表是纳秒级的，因此效率很高，适合做缓存
遍历的时间复杂度都是O(n)

hash就是md5算法加密，非常快，散列算法实现
hash和内存地址有映射关系
in操作的时间复杂度是O(n)，只需算出hash值去对应的内存地址中查看即可
hash相当于内存地址的门牌号码，因此比线性表查找速度快很多

线性数据结构，搜索的时间复杂度都是O(n)
hash表结构，内部使用hash作为key，时间复杂度是O(1)

内建数据类型中只有列表，字典，集合，bytearray是不可hash的类型

集合里面的元素本质是key，因此可以去重
!!!!对集合遍历就是对key遍历，如果遍历过程改变了集合的长度，则会抛出异常!!!!


'''


s1 = set()
print(s1)

s2 = set(range(5))
print(s2)

print({1, *range(3), 10})

# 增
s1.add('a')
print(s1)

s1.update(range(5), 'abc', [4, 5, 6])
print(s1)

s1.update(['abc', 20, 30])
print(s1)

# 删
s1.remove('a')
print(s1)


# 每次算出的hash都是一样的
print(hash('a'))
print(hash('a'))
print(hash('a'))
