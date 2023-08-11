'''
协程

有yield关键字的为生成器函数
遇到yield后函数暂停执行并可以返回出去

通常函数暂停是因为线程切换，时间片用完，线程进入就绪态
生成器函数暂停是开发人员通过yield决定

多个生成器函数在同一个线程中
但是如果生成器函数遇到IO阻塞，则无法继续执行其他生成器

'''

import string
import time


def count():
    x = 1
    while True:
        # print(x)
        yield x  # yield暂停
        x += 1
        if x > 30:
            break


def count2():
    s = string.ascii_lowercase
    for c in s:
        yield c


g1 = count()
g2 = count2()
tasks = [g1, g2]


while True:
    pop_index = []
    for i, task in enumerate(tasks):
        ret = next(task, None)  # 获取yield的值，如果遇到StopIteration则返回None
        if ret is not None:
            print(ret)
        else:
            pop_index.append(i)  # 不能动态循环中移除容器中内容，因此先记录索引

    # 在索引中逆序删除，否则会找不到索引
    for i in reversed(pop_index):
        tasks.pop(i)

    # 如果容器空了都退出了，则等待下一任务
    if len(tasks) == 0:
        time.sleep(1)
