import socket
import threading
import time


def acp():
    i = 0
    while True:
        new_sock, raddr = server.accept()  # 阻塞线程，等待连接进来
        # 把客户端套接字放到子线程中，不会阻塞在IO
        threading.Thread(target=recv, name=f'r{i}', args=(new_sock,)).start()
        i += 1


# 可能会一直阻塞在客户端发送数据，而不会执行accept，因此要把接受放到子线程

def recv(sock):
    while True:
        try:
            data = sock.recv(1024)  # 阻塞线程，等待用户输入
            print(data)
            if not data:
                break
            sock.send(f'I receive a {data.decode()} data'.encode())
        except Exception as e:
            print(e)


if __name__ == '__main__':

    server = socket.socket()
    addr = ('127.0.0.1', 9999)

    server.bind(addr)
    print("listen...")
    server.listen()

    # 1. accept()和recv()会阻塞主线程
    # while True:
    #     new_sock, raddr = server.accept()
    #     print(new_sock, raddr)
    #     print(new_sock.getpeername())
    #     print(new_sock.getsockname())
    #     data = new_sock.recv(1024)
    #     print(data)
    #     new_sock.close()

    print('多线程+IO阻塞'.center(30, '*'))

    # 放在子线程中，不会阻塞主线程

    threading.Thread(target=acp, name='accept').start()

    while True:
        time.sleep(5)
        print(threading.enumerate(), threading.active_count())
