'''

如果多线程运行，使用的是局部变量则安全
threading.local是线程安全，每个线程创建空间，互不干扰

'''

import threading
import time

global_data = threading.local()


def worker():
    global_data.x = 0
    for i in range(1000):
        time.sleep(0.0001)
        global_data.x += 1
    print(global_data.x, threading.currentThread().name)


for i in range(10):
    t1 = threading.Thread(target=worker, name=f'w{i + 1}')
    t1.start()

print('=' * 30)
