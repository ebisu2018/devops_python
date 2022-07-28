'''

客户端编程

'''

import socket
import threading


def chat():
    client = socket.socket()
    client.connect(('127.0.0.1', 9999))
    print(client.getpeername())
    # 返回字节数
    x = client.send(b'abcde')
    # 返回byte类型
    data = client.recv(1024)
    print(type(data), data)
    client.close()


class ChatClient:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.client = socket.socket()
        self.ipaddr = ip, port

    def start(self):
        try:
            self.client.connect(self.ipaddr)
            self.client.send(b'hello')
            threading.Thread(target=self.recv, name='recv').start()
        except Exception as e:
            print(e)
            raise

    def recv(self):
        while True:
            data = self.client.recv(1024)
            msg = data.decode()
            print(msg)

    def send(self, msg:str):
        self.client.send(msg.encode())

    def stop(self):
        self.client.close()


def inter(client: ChatClient):
    while True:
        msg = input('>>>')
        if msg == 'q':
            client.send('q')
            client.stop()
            break
        client.send(msg)


if __name__ == '__main__':
    client = ChatClient()
    try:
        client.start()
        threading.Thread(target=inter, name='inter', args=(client,)).start()
    except Exception as e:
        print(e)
