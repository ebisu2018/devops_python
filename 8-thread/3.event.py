'''

线程同步
如果多个核，每个核一个线程就是同一时刻的多线程运行
但是如果多线程处理同一个对象的时候会有线程安全问题

线程同步
避免多个线程争抢同一个资源
常用的技术有event和lock

Event，线程间通信机制，内部使用标记flag，通过flag来操作
适合场景 1V1护着1V多的通知
多个在wait()，1个做事完成后set()即可
set不设置，一直wait
而不需要保持长轮询
不管多少个线程，等待的是同一个event

wait(time)，可以接受一个时间数
如果超时则返回false，如果在时间期间设置了set，则wait函数返回True


'''


import threading

e = threading.Event()
print(e.is_set())
e.set()
print(e.is_set())
e.clear()


# 默认信号是False
event = threading.Event()


def boss(event):
    print('boss: watching')
    # 一直等待信号，直到信号为1
    event.wait()
    print('boss: good job')


def worker(event, count=10):
    print('worker: working')

    cups = []
    while not event.wait(0.5):
        cups.append(1)
        print(f'make {len(cups)} cup')
        if len(cups) >= count:
            # 任务完成后将设置信号为1
            event.set()
            break

    print(f'worker: done {len(cups)}')


w = threading.Thread(target=worker, name='worker', args=(event,))
w.start()
b = threading.Thread(target=boss, name='boss', args=(event,))
b.start()
