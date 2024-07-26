'''
set集合，是可变，无序，不重复的数据结构
frozenset 集合是不可变序列
无序就没有索引，非线性容器

!!!!!set中的元素只能是可hash对象（不可变的数据类型）!!!!!
集合无法存储列表、字典、集合，bytearray这些可变数据类型
内建数据类型中 列表，字典，集合，bytearray 是不可hash， hash()

创建set，注意元素去重
用{}创建，*空{}是字典不是集合
set()，创建空集合
set(iterable)

增
只能是数字、字符串、元组或者布尔类型（True 和 False）值
add()，把一个元素直接添加到集合中，必须是不可hash的类型
update()，把可迭代对象中元素一一增加到集合中

删除
remove()，如果没找到则KeyError，因为元素是hash key
discard()，有则删除没有也不会抛出KeyError
clear()，清空集合
pop()，随机弹出一个

没有索引所以无法改，只能先删除再新增

查
in 成员标识符，判断是否在集合中

效率
hash表是纳秒级的，因此效率很高，适合做缓存
线性数据结构，in的时间复杂度都是O(n)
hash表结构，内部使用hash作为key，时间复杂度是O(1)

hash就是md5算法加密，散列算法实现，hash和内存地址有映射关系
in操作的时间复杂度是O(n)，只需算出hash值去对应内存地址中查看即可
hash相当于内存地址的门牌号码，因此比线性表查找速度快很多

!!!!对集合遍历就是对key遍历，如果遍历过程改变了集合的长度，则会抛出异常!!!!
'''

print('创建set'.center(30, '#'))
print({True, 1})  # 去重，因此True和1只留一个
s1 = set()
print(s1)
s2 = set(range(5))
print(s2)
print({1, *range(3), 10})

print('添加'.center(30, '#'))
s1.add((1, 2))
print(s1)

s1.update(range(5), 'abc', [4, 5, 6])
print(s1)
s1.update(['abc', 20, 30])
print(s1)

print('删除'.center(30, '#'))
s1.remove('a')
s1.discard('x')
print(s1.pop()) # 没有索引，不是最后一个，随机弹出并返回
print(s1)
s1.clear()
print(s1)

# 每次算出的hash都一样
print(hash('a'))
print(hash('a'))

print('交集并集差集'.center(30, '#'))
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# 交集
print(set1 & set2)

# 并集
print(set1 | set2)

# 差集，取一个集合在另一集合中没有的元素
print(set2 - set1)

# 对称差集，取集合 A 和 B 中不属于 A&B 的元素
print(set1 ^ set2)
