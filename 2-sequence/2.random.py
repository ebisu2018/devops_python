'''
random模块用来获取随机数

shuffle(list), 对一个列表内容进行打乱
randint(start, end),返回[start, end]的随机数
randrange(start, end), 返回[start, end)的随机数
choice(list), 从列表中随机取出一个元素
choices(list), 从列表中取出一个或者多个，并用列表返回，默认k是1取1个，可以重复取，可以指定权重
sample(list), 和choices类似，但是不可以重复采样

'''

import random

a = list(range(5))
random.shuffle(a)
print(a)

for i in range(5):
    print(random.randint(0, 1))

for i in range(5):
    print(random.randrange(0, 1))

for i in range(5):
    print(random.choice(a))

print(random.choices(a, k=10))

for i in range(5):
    print(random.sample(a, k=3))