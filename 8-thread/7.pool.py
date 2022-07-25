'''

异步并行

提供2个池

异步调用的线程池
异步调用的进程池



'''
import threading
from concurrent.futures import ThreadPoolExecutor
import time

def cal(base):
    s = base
    for i in range(1000000):
        s += 1

    return s


# 创建一个异步线程池，最大3个
executor = ThreadPoolExecutor(3)
future = executor.submit(cal, 100)


while True:
    time.sleep(1)
    print(threading.enumerate())
