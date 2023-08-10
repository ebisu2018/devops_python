'''

Socket编程

套接字编程，通用的网络编程接口，实现对底层网络接口的封装
socket模块是非常底层的接口库
在网络协议出现之后为了更方便的实现网络IO，把网络IO抽象出来实现
基于网络协议之上的，高级抽象，方便的网络编程接口，而不是从底层开发

为什么需要socket：不同应用进程之间需要借助网络端口通道来解决端到端通信
IP地址在网络层工作，套接字在传输层工作

accept只是用来接受客户端的请求进来
！！！！真正实现socket和客户端通信的是返回的新socket对象！！！！


AF是Address Family简称，有AF_INET的IPv4 和 AF_INET6的IPv6
SOCK_STREAM，面向连接的TCP连接
SOCK_DGRAM，无连接的UDP连接

服务端编程流程：
创建socket对象
bind地址和端口
listen进行监听，实现三次握手连接
accept，建立连接后接受客户端并底层创建新的socket对象和客户端通信
recv和send，用新的socket对象和客户端通信

还可以用makefile()是生成文件对象，用文件对象做IO
读写模式是rw，读写返回的都是字符串类型

很多方法都是阻塞，因此用多线程


'''

import socket

# 创建socket对象，默认是IPv4，TCP连接
server = socket.socket()

# 监听的地址和端口
addr = ('127.0.0.1', 9999)

# 绑定到服务端
server.bind(addr)

# 开启服务端监听，不会阻塞线程，做三次握手用
server.listen()


print('accept'.center(30, '#'))
# 阻塞方法，等待连接，如果有连接来则返回新的socket对象
# accept返回一个新的socket对象和一个客户端元组
newsock, raddr = server.accept()
print(newsock, raddr)
print(newsock.getpeername())
print(newsock.getsockname())


# 1. 用recv和send的方法
# # 接受数据，是阻塞方法，没收到数据会一直等，直到收到数据会返回
# 如果要一直收发，则发到while循环中
# recv返回的是byte类型
data = newsock.recv(1024)
print(type(data), data)

# # 发送数据给客户端，发送数据需要用byte类型
newsock.send(f'!!!!{data.decode()}!!!'.encode())


# print('makefile'.center(30, '#'))
# 2. 用makefile的rw方法作为文件对象读写
# nf = newsock.makefile('rw')
# data_str = nf.read(5)
# print(type(data_str), data_str)
#
# nf.write('ACK')


# # 关闭连接
newsock.close()
server.close()
# nf.close()
