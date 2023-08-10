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
这个过程全程阻塞，成为阻塞IO
内存分为2部分，一部分给内核使用，另一部分给用户态使用

同步异步强调结果
同步：没有结果则等待
异步：不等结果并继续做其他事

阻塞非阻塞强调行为，卡没卡主

分类：
同步阻塞IO：一定要拿到结果才继续，否则一直等待结果而卡主
同步非阻塞IO：不常用，没有卡主，但要轮询查询结果
异步阻塞IO：不常用，不等待结果，并且阻塞住
异步非阻塞IO：不等待结果继续做其他事情，后端返回中间结果，待有结果回调函数返回结果
IO多路复用，事件驱动IO，重要！




IO多路复用：
多线程成本高总是反复创建线程，用户不好管理，交给selector
使用OS提供的功能管理IO
通过Selector管理多路IO

selector，分为select，poll，epoll模型
让操作系统帮程序监控而不是程序一直阻塞

注册IO到selector，进程阻塞，内核监视注册的fd，如果fd的IO有数据，selector返回
调用read将数据复制到用户空间

每一个item包含fobj，fd，event，data
fobj就是socket对象

要关注register和select的内容
只要一个while循环，来循环select中的内容，而recv中不用循环

'''

import selectors
import socket
import threading


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


if __name__ == '__main__':

    server = socket.socket()
    server.bind(('localhost', 9999))
    server.listen()
    server.setblocking(False)

    # 根据操作系统选择合适的selector
    selector = selectors.DefaultSelector()

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
