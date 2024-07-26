'''
解析式
解析式会构建一个新的列表或集合或字典
只能有if，不能有else表达式

在中括号中是列表解析式
在大括号中是字典解析式或者集合解析式
在小括号中是生成器表达式！

生成器表达式：
(表达式 for 迭代变量 in 可迭代对象 [if 条件表达式] )
在小括号中构建的解析式，是生成器对象
生成器对象属于迭代器
map(), filter(), reversed()也属于迭代器

创建生成器对象2种方式
1. 生成器表达式


！！！！迭代器特点！！！！
1.一次性迭代，有指针
2.是惰性的，必须调用__next__()计算
3.for循环可以迭代，如果到尽头不会异常for会处理一场；如果到尽头再调用__next__，会抛出stopIteration异常
4.迭代器没有索引，因为可能有无限个元素！但是列表必须是有明确的长度边界！

可迭代对象：list，dict，tuple，set，string，range
可迭代对象不属于迭代器，因为有索引并可以重复迭代

列表会在内存中立刻构建，元素都生成出来，占用空间，但是获取元素快
生成器属于懒加载延迟计算，内存中只生成生成器对象，调用__next__时才构建元素返回，节省空间，但是需要计算再返回

reversed(seq)，返回的是迭代器，倒序迭代器
sorted(iterable, key=fn, reverse=False)函数，返回一个有序列表，可以指定升序降序
key是函数，可迭代对象作为参数，仅用于进行比较，最终类型不会改变
reverse指定升序倒序
'''
import random
import string

print('列表解析式'.center(30, '='))
print([i ** 2 for i in range(5)])
print([i ** 2 for i in range(5) if i % 2])
print([(i, j) for i in range(5) for j in range(3)])


print('集合解析式'.center(30, '='))
print({i * 2 for i in range(5)})

print('字典解析式'.center(30, '='))
print({i: j for i in 'abc' for j in range(3)})
print({k: len(k) for k in ['python', 'golang']})


print('生成器表达式'.center(30, '='))
a = (x for x in range(1, 5))
print(a)

print(a.__next__())
print(next(a))

# 只能遍历一次！
print(tuple(a))


print('内建函数'.center(30, '='))
print([str(i) for i in range(5)])
print(map(str, range(5)))

f = filter(lambda x: x > 5, range(1, 10))
print(f, list(f))

print(sorted((i for i in range(5))))
print(sorted(dict(a=1, b=2)))
print(sorted((i * 2 for i in range(5)), reverse=True))

sites = ['China',
         'USA',
         'Italy',
         'Spain',
         'Germany']
print(sorted(sites, key=lambda x: len(x)))

z = zip([11, 12, 13], (21, 22, 23))
print([i for i in z])

# 生成产品ID
for i in range(10):
    num_ls = list()
    for j in range(6):
        num = random.randrange(10)
        num_ls.append(str(num))
        num_of_id = sorted(num_ls)
    str_of_id = random.choices(string.ascii_lowercase, k=10)
    print(f'{''.join(num_of_id)}.{''.join(str_of_id)}')
