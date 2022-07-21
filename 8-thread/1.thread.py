'''

1. 并行parallel，同时做某事，同一时刻做几件事
相当于银行开多个窗口处理，解决单个窗口拥挤的事情
2. 并发concurrency，强调一段时间内要处理事情，如果一段时间处理很多，则是高并发
相当于银行一个窗口一段时间需要处理多个事

并行本质是用水平方式来解决高并发

进程，内存中运行的程序，存放指令和数据，是线程的容器，资源的管理者
线程，进程中程序执行流的最小单位，可以有一个或者多个，是工作的执行者
进程中的线程之间共享资源，进程之间不共享数据，但是进程之间可以通信
线程有自己独立的堆栈，函数调用需要用栈

由操作系统来分配进程以及管理调度线程
线程的状态
1. Ready，等待CPU调度
2. Running，从Ready中调度，线程正在CPU中运行
3. Blocked，等待外部事件而阻塞线程运行，处理完后会进入到Ready状态
4. Terminated，线程执行结束

CPU在同一个时间只能运行一个线程，如果有多核则同一时间多个线程，每个核上一个线程
并行只是表现出来的，只是时间片切换的太快，看上去是并行

主线程是第一个启动的，至少有一个主线程，其他线程是工作线程
线程异常了会抛出，需要在线程中捕获异常
多线程的target是函数，哪个线程调用，则函数属于哪个线程！
函数中不能获取返回值

线程对象只能start一次
start()方法本质是创建一个工作线程，并关联目标函数
run()方法本质是执行目标函数
必须调用start而不是run

多线程最大的问题是线程安全问题

daemon参数
non daemon线程，表示主线程结束会等待daemon线程执行完，默认是False
daemon线程，主线程运行结束后，不会等待daemon线程，和其他线程一起退出
结不结束程序取决于主线程是否还在运行

线程对象.join()，阻塞其他线程并等待该线程对象执行
让当前线程对象先执行，并阻塞其他线程

'''

import threading
import time


def worker():
    for i in range(10):
        time.sleep(1)
        print('+' * 30)


def add(a, b):
    # print(threading.main_thread(), threading.currentThread())
    print('start')
    time.sleep(2)
    print(a + b)
    print('end')


# 创建线程对象，参数可以在args或者kwargs中
t = threading.Thread(target=add, name='add', args=(2, 3))
# 启动线程
# t.start()

# print(threading.main_thread(), threading.currentThread())

print('自定义线程')


class MyThread(threading.Thread):
    def start(self) -> None:
        super().start()
        print('start~~~~~~~~~')

    def run(self) -> None:
        super().run()
        print('run~~~~~~~~~')


t1 = MyThread(target=worker, name='worker')
t1.start()
# t1.join()
print('=' * 30)
