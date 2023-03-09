from socketserver import ThreadingTCPServer, BaseRequestHandler
import io


# 1.函数实现app
def application(environment, start_response):

    method = environment.get('method')
    # 根据path可以路由
    path = environment.get('get')
    if path == '/index' and method.lower() == 'get':
        start_response("200 OK", [
            ('Content-type', 'text/html; charset=utf-8'),
            ('X-MYSERVER', 'Pablo')
        ])
        with open('templates/index.html', encoding='utf-8') as f:
            html = f.read()
        html = html.format(test='Hello')
        return [html]


# 2.类实现app，对象必须返回可迭代对象
class Application:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        self.start_response("200 OK", [
            ('Content-type', 'text/html; charset=utf-8'),
            ('X-MYSERVER', 'Pablo')
        ])

        with open('templates/index.html', encoding='utf-8') as f:
            html = f.read()
        html = html.format(test='Hello')

        return iter((html,))


# 3.对象调用实现app
class App:
    def __call__(self, environ, start_response):
        return application(environ, start_response)


# WSGI Server实现
class HTTPHandler(BaseRequestHandler):

    def start_response(self, status, headers):

        # 拼凑响应头
        res_headers = []
        firstline = "HTTP/1.1 " + status
        res_headers.append(firstline)
        for k, v in headers:
            res_headers.append(f"{k}: {v}")
        else:
            res_headers.append('')
            res_headers.append('')

        header = '\r\n'.join(res_headers)
        print(header)
        self.request.send(header.encode())

    def handle(self) -> None:
        data = self.request.recv(1024)
        # print("data:", data)
        # 拼凑请求头，实际开发中environ一般是一个request对象
        environ = dict()
        firstline, others = data.decode().split('\r\n', 1)
        method, path, protocol = firstline.split()
        environ['method'] = method
        environ['path'] = path
        environ['protocol'] = protocol
        for line in others.split('\r\n'):
            if line:
                k, v = line.split(': ', 1)
                environ[k] = v

        ret = application(environ, self.start_response)
        print(ret)
        sio = io.StringIO()
        for i in ret:
            print(i, file=sio)
        self.request.send(sio.getvalue().encode())


server = ThreadingTCPServer(('127.0.0.1', 8080), HTTPHandler)
server.serve_forever()
