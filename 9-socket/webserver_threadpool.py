import concurrent.futures
import socket
import threading
import time

'''
http web server模型

线程池

解决高并发场景频繁创建线程
'''


# 拼接response报文

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>服务端返回的数据</h1>
</body>
</html>
'''.encode()

response = '''
HTTP/2 200 OK
server: Xavier
Date: Sat, 05 Aug 2023 04:15:07 GMT
Content-Type: text/html
Content-Length: {}
Connection: keep-alive

'''.format(len(html)).replace('\n', '\r\n').encode() + html


# 创建线程池，设置最大1024，懒创建，需要的时候才创建
executor = concurrent.futures.ThreadPoolExecutor(1024)

# 进程池，创建多个进程，代价太高
# executor = concurrent.futures.ProcessPoolExecutor(10)


def acp():
    while True:
        new_sock, raddr = server.accept()

        # 利用线程池库帮助管理线程
        executor.submit(recv, new_sock)


def recv(sock):
    try:
        data = sock.recv(1024)
        if not data:
            raise ConnectionError
        sock.send(response)
    except Exception as e:
        print(e)
    finally:
        sock.close()


if __name__ == '__main__':

    server = socket.socket()
    addr = ('127.0.0.1', 9999)

    server.bind(addr)
    server.listen(1024)
    executor.submit(acp)

    while True:
        time.sleep(5)
        print(threading.active_count())
