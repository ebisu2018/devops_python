'''

Lock
解决线程同步的技术
相当于排队的ATM取钱原理
acquire()方法会锁定当前线程，其他线程如果acquire则会被阻塞等待状态
除非锁的线程被release

如果lock的锁没有release就退出，则会一直占用着线程，其他线程会一直阻塞

如果使用全局变量操作
由于没有上锁，导致获取变量的时候其他线程也在操作该变量导致数据错误

一定要搞清楚在哪里上锁，在哪里解锁

在判断和生产的地方加锁解锁，就像闸口一样

lock有上下文，已经实现了enter和exit的方法，离开with会release
锁的地方尽量短，避免死锁


GIL，全局解释器锁
即使一个CPU多个物理核心，Cpython保证只有1个进程的1个线程在其中一个物理核心上运行！
其他的线程被锁住不能在其他核心上运行
只要有一个进程的线程在一个核上运行，其他线程都被锁住不能在其他核上运行，但不一定一个线程一直在一个核上运行
对进程内的线程有限制而已
因此python是假的并行
python当中对计算密集型，多线程不如单线程

'''

import threading
import time

# 创建锁对象
lock = threading.Lock()

# 查看是否是锁定状态
# print(lock.locked())

# 获取锁，返回True，代表锁住了
# print(lock.acquire())

# 释放
# lock.release()


cups = []


# 没有上锁的代码线程不安全的
def worker(count=100):
    print('start to make the cup')
    while True:
        # lock.acquire()
        with lock:
            if len(cups) >= count:
                # lock.release()
                break
            time.sleep(0.01)
            cups.append(1)
        # lock.release()
    print(f'{threading.currentThread().name} finished, cups={len(cups)}')


for i in range(10):
    threading.Thread(target=worker, name=f'w-{i}').start()
