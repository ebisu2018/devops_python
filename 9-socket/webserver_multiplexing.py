import selectors
import socket

'''
IO多路复用

IO多路复用

生成默认的选择器，根据不同的OS会有不同种类的选择器

注册三个参数：带fd的socket对象，EVENT对象，data

返回的是key，有fileobj，fd，events，data

'''


html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>服务端返回的数据 IO多路复用</h1>
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


def fn2(conn: socket.socket):
    print("call fn2")
    try:
        data = conn.recv(1024)
        if not data:
            print("bye")
        conn.send(response)
    except Exception as e:
        print(e)
    finally:
        # 关闭连接前要取消注册，不用系统监控
        selector.unregister(conn)
        conn.close()


def fn(s: socket.socket):
    print("start accept")
    conn, raddr = s.accept()
    s.setblocking(False)
    selector.register(conn, selectors.EVENT_READ, fn2)


if __name__ == '__main__':

    server = socket.socket()
    server.setblocking(False)  # 提交给多路选择器应该是非阻塞IO
    server.bind(('127.0.0.1', 9999))
    server.listen(1024)

    # 创建多路选择器，windows下只有select
    selector = selectors.DefaultSelector()

    # 向操作系统注册fd，包装的key就是server对象
    key = selector.register(server, selectors.EVENT_READ | selectors.EVENT_WRITE, fn)
    # print(key.fileobj, server == key.fileobj)
    # print(key.fd)
    # print(key.events)
    # print(key.data)

    while True:
        # 阻塞主线程，注册的IO有事件(读或者写)发生则停止阻塞，返回列表
        event_list = selector.select()

        for key, mask in event_list:
            print('fd:', key.fd)
            key.data(key.fileobj)
