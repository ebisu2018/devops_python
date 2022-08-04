'''

IO
一个进程在内存中的模型
用户空间：想用内核空间的数据需要从内核态复制过来
内核空间：只操作系统内核使用，被保护的

CPU级别：
ring0，级别最高，可以使用所有范围内存，特权指令如系统调用
ring3，用户指令，只在用户空间使用

IO的两个阶段：
从设备读取数据到内核空间缓冲区
从内核空间的数据复制到用户空间缓冲区

分类：
阻塞IO，同步阻塞IO，比如socket的recv，需要多个线程，切换线程代价高
非阻塞IO，同步非阻塞IO，效率低，总是轮询，少用
IO多路复用，事件驱动IO，重要！

IO多路复用：
OS代替而不用自己阻塞或者轮询
事件驱动，如果数据到了会中断
select可以注册很多事件

bio就是同步IO
aio就是异步IO

selector
让操作系统帮程序盯着而不是程序一直阻塞等待数据
数据到来会通知程序

需要把socket对象register到selector中
其中data是一个标识符用来给程序判断用，可以是任意类型

调用select方法开始监听，返回的是列表对象
每一个item包含fobj，fd，event，data
fobj就是socket对象

要关注register和select的内容
只要一个while循环，来循环select中的内容，而recv中不用循环

好处：不用开辟过多的线程，只在主线程即可

'''

import selectors
import socket
import threading

server = socket.socket()
server.bind(('localhost', 9999))
server.listen()
server.setblocking(False)


# callback
def recv(s, mask):
    data = s.recv(1024)
    print(data)
    msg = 'From {}:{}. data = {}'.format(*s.getpeername(), data)
    s.send(msg.encode())


def accept(s, mask):
    new_sock, raddr = s.accept()
    print(new_sock)
    new_sock.setblocking(False)
    # 在这里注册
    k = selector.register(new_sock, selectors.EVENT_READ, recv)
    print(k)


# 根据操作系统选择合适的selector
selector = selectors.DefaultSelector()
print(selector)
# 向selector注册，返回fobj，fd，events，data标识
key = selector.register(server, selectors.EVENT_READ | selectors.EVENT_WRITE, accept)
print(key)

while True:
    # 开始让selector代替盯着，如果有一个连接来则立即返回
    events = selector.select()
    print('events is', events)

    # key是监听到的对象，可以通过key获取到socket对象然后accept和send
    for key, mask in events:
        print(key.fileobj, key.fd)
        key.data(key.fileobj, mask)
    print(threading.enumerate())
