'''

正常情况，解释器是顺序执行代码
条件判断

一般先写好if，在代码块中可以写pass # TODO

容器就是可迭代对象
迭代/遍历：将容器中的元素只拿出一次

range(n),属于惰性对象，必须要迭代才能取出里面的元素，否则只返回一个可迭代对象
如果n<=0，则只有空容器，里面没有元素

都是作用在循环中的条件判断中
continue，是结束当前循环，开始下一次循环
break，退出当前循环

else在for循环之后正常执行，如果没有遇到break

三元表达式
真对应表达式 if condition else 假对应表达式

'''

if True:
    pass # TODO

# a = input('>>>')
# while a:
#     print(a)
#     a = input('>>>')

# for i in range(5):
#     print(i + 1)

# 空容器
for i in range(0):
    print(i)

# 第三个参数指定方向和间隔，负号代表方向
# for i in range(1, -5, -1):
#     print(i)
#
# for i in range(0, 5, 2):
#     print(i)
#
# for i in range(1, 5, 2):
#     print(i)

# 1开始到1000，前18个，7的倍数
count = 1
for i in range(7, 1000, 7):
    if count == 11:
        break
    print(count, i)
    count += 1

for i in range(5):
    if i > 3:
        continue
    print(i)
else:
    print('end')

for i in range(5):
    if i > 3:
        break
    print(i)
else:
    print('end')
