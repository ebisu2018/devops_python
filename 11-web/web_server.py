'''

WSGI实现

WSGI需要提供environment和start response参数给应用
应用要先根据start response返回response的header然后再返回body

'''
import json
from socketserver import ThreadingTCPServer, BaseRequestHandler
import io


def application(environ, start_response):
    if environ.get('path') == '/index':
        start_response('200 OK',
                       [('Content-type', 'text/html; charset=utf-8'),
                        ('X-SERVER', 'Demo')])

        with open('webapp/templates/index.html', encoding='utf-8') as f:
            content = f.read()
        html = content.format(domain='NiuNiu')
    else:
        start_response('200 OK',
                       [('Content-type', 'application/json; charset=utf-8'),
                        ('X-SERVER', 'Demo')])

        res = {'count': 100, 'results': [{'name': 'Pablo', 'age': 30}]}
        html = json.dumps(res)

    return [html]


# application必须要返回可迭代对象
class Application:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        self.start_response('200 OK',
                       [('Content-type', 'text/html; charset=utf-8'),
                        ('X-SERVER', 'Demo')])

        with open('webapp/templates/index.html', encoding='utf-8') as f:
            html = f.read()
        html = html.format(domain='NiuNiu')
        return iter((html,))


class HTTPHandler(BaseRequestHandler):

    # 处理响应头
    def start_response(self, status, headers):
        res_headers = []
        first = 'HTTP/1.1 ' + status
        res_headers.append(first)
        for k, v in headers:
            res_headers.append(f'{k}: {v}')
        else:
            res_headers.append('')
            res_headers.append('')

        response_headers = '\r\n'.join(res_headers)
        # print('response header is', response_headers)
        self.request.send(response_headers.encode())

    def handle(self) -> None:
        data = self.request.recv(1024)
        # print(data)

        # 先包装environment
        environ = {}
        firstline, others = data.decode().split('\r\n', 1)
        method, path, protocol = firstline.split()
        environ['method'] = method
        environ['path'] = path
        environ['protocol'] = protocol
        for line in others.split('\r\n'):
            if line:
                k, v = line.split(': ', 1)
                environ[k] = v
        # print(environ)

        # 通过函数调用application
        # ret = application(environ, self.start_response)

        # 通过类调用application
        ret = Application(environ, self.start_response)
        sio = io.StringIO()
        for c in ret:
            print(c, file=sio)
        self.request.send(sio.getvalue().encode())


server = ThreadingTCPServer(('127.0.0.1', 8080), HTTPHandler)
server.serve_forever()
