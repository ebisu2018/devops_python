'''

多进程

多进程代码必须放在main中
进程会占用很多内存空间




'''

import multiprocessing


def cal():
    s = 0
    for i in range(10000):
        s += 1


if __name__ == '__main__':
    ps = []
    for i in range(3):
        p = multiprocessing.Process(target=cal, name=f'p-{i}')
        ps.append(p)
        p.start()

    for p in ps:
        p.join()
