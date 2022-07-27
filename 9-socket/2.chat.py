'''

点到点聊天通信

'''

import socket
import threading


class ChatServer:

    def __init__(self, ip='127.0.0.1', port=9999):
        self.addr = ip, port
        self.sock = socket.socket()
        self.event = threading.Event()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        # 防止主线程阻塞
        threading.Thread(target=self.accept, name='accept').start()

    # accept会在一个线程中循环监听连接，如果有连接进入则会开辟新线程
    def accept(self):
        while not self.event.is_set():
            new_sock, raddr = self.sock.accept()
            threading.Thread(target=self.recv, name='recv', args=(new_sock, raddr)).start()

    def recv(self, sock, raddr):
        while not self.event.is_set():
            data = sock.recv(1024)
            if data == b'' or data == b'q':
                break
            sock.send('from {}, data is {}'.format(*raddr, data).encode())

    def stop(self):
        self.event.set()
        self.sock.close()


if __name__ == '__main__':
    cs = ChatServer()
    cs.start()
    while True:
        cmd = input('>>>')
        if cmd == 'q':
            cs.stop()
            break
