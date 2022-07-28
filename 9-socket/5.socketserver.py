'''

socket模块过于底层，编程语言会对其进行封装成高级模块
socketserver就是python封装的

需要自己实现handler类
BaseRequestHandler的三个参数
request：是accept后的socket，用来和客户端通信
client address：是远端客户的socket
server：是实例化后的TCPServer对象

初始化BaseRequestHandler
是当accept了后，拿到新的socket和raddr对象后才初始化

TCPServer()会做绑定，监听
handle_request()，实际调用accept()

'''

import socketserver
import threading


class MyHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        print(self.request) # accept的socket对象和客户通信
        print(self.client_address) # raddr
        print(self.server) # TCPServer对象

        while True:
            data = self.request.recv()
            msg = 'from {}:{}: {}'.format(*self.client_address, data)
            self.request.send(msg.encode())

# 单线程的
# server = socketserver.TCPServer(('localhost', 9999), MyHandler)

# 有多线程的，避免单线程出现阻塞
server = socketserver.ThreadingTCPServer(('localhost', 9999), MyHandler)

# accept
# server.handle_request()

# 永远阻塞accept
# server.serve_forever()

# 放到线程中
threading.Thread(target=server.serve_forever, name='forever').start()