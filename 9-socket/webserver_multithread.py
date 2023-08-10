import socket
import threading

'''
http web server模型

缺点是不断创建销毁线程，不适用高并发场景
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


def acp():
    while True:
        new_sock, raddr = server.accept()
        threading.Thread(target=recv, name='r', args=(new_sock,)).start()


# 可以使用第三方库解析http请求，提取URL，open打开找到资源为字符串返回给客户端


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
    print('listen...')
    server.listen(1024)

    print('start to accept...')
    threading.Thread(target=acp, name='accept').start()
