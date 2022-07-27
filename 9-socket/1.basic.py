'''

Socket套接字，通用的网络编程接口，实现对底层网络接口的封装
在网络协议出现之后为了更方便的实现网络的IO而实现socket编程
基于网络协议之上的，高级抽象，方便的网络编程接口，而不是从底层开发

应用的进程之间需要借助网络端口搭通道来解决端到端通信


参数：
AF是Address Family，有AF_INET的IPv4 和 AF_INET6的IPv6
SOCK_STREAM，面向连接的TCP
SOCK_DGRAM，无连接的UDP

服务端编程流程：
创建socket对象
bind地址和端口
listen进行监听，实现三次握手连接
accept，建立连接后接受客户端并底层创建新的socket对象和客户端通信
返回元组类型，有对端和本地的ip地址和端口号
recv和send，用新的socket对象和客户端通信

很多方法都是阻塞，因此用多线程比较好


'''

import socket

# 创建socket对象
server = socket.socket()
print(server)

# 监听的地址和端口
addr = ('127.0.0.1', 9999)

# 绑定到服务端
server.bind(addr)

# 开启服务端监听，不会阻塞，做三次握手的搭链接
server.listen()

# 阻塞方法，等待连接，如果有连接来则返回新的socket对象
newsock, raddr = server.accept()
print(newsock, raddr)
print(newsock.getpeername())
print(newsock.getsockname())
print('accept'.center(30, '#'))

# 1. 用recv和send的方法
# # 接受数据，是阻塞方法，没收到数据会一直等，直到收到数据会返回
data = newsock.recv(1024)
print(type(data), data)

# # 发送数据给客户端
newsock.send(f'!!!!{data.decode()}!!!'.encode())

print('makefile'.center(30, '#'))
# 2. 用makefile的rw方法作为文件对象读写
nf = server.makefile('rw')
data_str = nf.read(5)
print(type(data_str), data_str)

nf.write('ACK')
nf.close()

# # 关闭socket连接
newsock.close()
server.close()
