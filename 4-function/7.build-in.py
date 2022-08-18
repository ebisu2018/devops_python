'''

迭代器特点
不会立即占用内存，是惰性的，只在需要的时候使用next方法计算出来
是指针的，只会迭代一次，迭代完之后就没了，即使用for循环再迭代，也没有任何输出


一些有用的内建函数

iter()，把可迭代对象包装成迭代器
next()，迭代器或者生成器才有的方法，如果到头了会抛出异常，可以指定异常时候的默认值

reversed()，生成迭代器，倒着读而不是倒序！效率高，只支持seq

enumerate()，生成迭代器，返回索引和值，支持集合

sorted(),是一个升序排列的列表！

filter(condition，iterable)，把可迭代对象中元素一一做条件判断，过滤出不符合条件的，返回的是迭代器

map(lambda, iterable)，把可迭代对象中元素处理成另一种形式，返回迭代器

zip()，和每个集合的对应元素组合成元组返回的迭代器


eval() 和 exec() 都可以执行一个字符串形式的 Python 代码（代码以字符串的形式提供），
二者不同之处在于，eval() 执行完要返回结果，而 exec() 执行完不返回结果
只有在 globals 字典和 locals 字典作用域内的函数和变量才能被执行


'''


l = [0, 1, 2, 3, 4, 5]
i1 = iter(l)
print(i1)
for i in i1:
    print(i)

for i in i1:
    print(i)

print(reversed(l))
for i in reversed(l):
    print(i)

e = enumerate(l)
for i in e:
    print(i)


print('filter')
x = filter(lambda x: x % 2, range(5))
print(list(x))

m = map(lambda x: x ** 2, range(5))
print(list(m))

print(list(map(lambda *args: args, range(5), 'abcd')))

z = zip('abcd', range(5), '1234')
for i in z:
    print(i)

