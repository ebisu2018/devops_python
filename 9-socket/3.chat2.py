'''
群聊客户端
把每次的socket保存起来

线程安全问题
即使是多个线程，依然可以对同一个字典遍历不会影响
不管有没有GIL，大多数都是假并行，因为核少，进程多，不可能所有的核都运行同一个进程的线程

但是不能多个线程遍历字典的同时修改字典的长度
字典和集合不能在遍历过程中修改长度！

使用锁会安全，但是客户端增多就不好了，时间会很慢


'''

import socket
import threading


class ChatServer:

    def __init__(self, ip='127.0.0.1', port=9999):
        self.addr = ip, port
        self.sock = socket.socket()
        self.event = threading.Event()
        self.clients = dict()
        # 互斥锁，防止遍历过程中修改字典长度
        self.lock = threading.Lock()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        # 防止主线程阻塞
        threading.Thread(target=self.accept, name='accept').start()

    # accept会在另一个线程中循环监听连接，不会阻塞主线程
    def accept(self):
        count = 1
        while not self.event.is_set():
            new_sock, raddr = self.sock.accept()
            with self.lock:
                self.clients[raddr] = new_sock
            # 接受数据在新线程中，不会阻塞当前accept
            threading.Thread(target=self.recv, name=f'recv-{count}', args=(new_sock, raddr)).start()
            count += 1

    def recv(self, sock, raddr):
        while not self.event.is_set():
            data = sock.recv(1024)
            if data == b'' or data == b'q':
                with self.lock:
                    self.clients.pop(raddr)
                    sock.close()
                break
            # 遍历所有的面向客户端的socket
            with self.lock:
                for s in self.clients.values():
                    s.send('from {}, data is {}'.format(*raddr, data).encode())

    def stop(self):
        self.event.set()
        with self.lock:
            for s in self.clients.values():
                s.close()


if __name__ == '__main__':
    cs = ChatServer()
    cs.start()
    while True:
        cmd = input('>>>')
        if cmd == 'q':
            cs.stop()
            break
