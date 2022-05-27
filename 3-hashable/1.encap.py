'''
封装与解构

右边的表达式先封装成元组再给前面的标识符
个数必须匹配，不能多也不能少

剩余标识，是把剩余的放到列表中返回
如果没有剩余则返回空列表
只能有1个剩余参数，并且不能单独出现剩余参数

如果可迭代对象前有*，则标识解构，表示把可迭代对象给拆开！

'''

a, b = 1, 2
print(a, b)

c = 1, 2
print(c)

a, b, c = range(3)
print(a, b, c)

a, b = {'a', 'b'}
print(a, b)

a, b = {'a': 10, 'b': 20}
print(a, b)


# 剩余
a, *rest, b = range(10)
print(a, rest, b)

a, *rest, b = range(2)
print(a, rest, b)

a, b = [1, [2, 3]]
print(a, b)

a, [b, c] = [1, [2, 3]]
print(a, b, c)


# _标识不关心标识符是什么
a, *_ = 1, 2, 3
print(a, _)

x = [*(1, 2)]
print(x)

x = [*range(5)]
print(x)

print([1, *range(4), 5])

path = '/user/local/admin/file.txt'
dirname, _, basename = path.rpartition('/')
print(dirname, _, basename)


