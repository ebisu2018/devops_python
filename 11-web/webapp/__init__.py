'''

ORM 对象关系映射
将请求对象和数据库中表做映射，Django中有ORM，Flask中没有
Flask中用Sqlalchemy，模板用Jinja2，blueprint

flask
就是定义路由在装饰器中
编写handler，通过调用模板来生成html
一般返回的不是html就是json的格式

返回的格式
可以直接返回字符串
也可以包装在Response对象中，因为可以添加header和status code

blueprint是模块化用的
把相应的功能分开


'''


from flask import Flask, request, Request, Response, jsonify, json, render_template
from .books import book

app = Flask('webapp')
app.register_blueprint(book, url_prefix='/book')


# 默认是Get请求，还有HEAD OPTIONS
# flask中只要处理返回的内容，可以编写返回码，如果需要添加header也可以
@app.route('/')
@app.route('/index', methods=['get', 'post'])
def index():
    # ret = Response('abc', status=201)
    page = render_template('index.html')
    ret = Response(page)
    ret.headers.add_header('X-Study', 'Java')
    return ret


@app.route('/json', methods=['Get', 'Post'])
def get_json():
    print(request.path)
    print(request.content_type)
    print(request.form)
    # print(request.query_string)
    print(request.args)
    ret = {
        'count': 2,
        'result': [
            (1, 'Pablo', 20),
            (2, 'Fernando', 30)
        ]
    }
    # return Response(json.dumps(ret), content_type='application/json')
    res = jsonify(ret)
    res.status = 200
    return res


@app.route('/index.js')
def get_jsonp():
    print(request.args)

    # 获取回调函数名
    cb = request.args.get('callback')
    resp = Response(f'{cb}({{a: 100, b: 200, c: 300}})')
    resp.content_type = 'application/javascript'
    return resp


# @app.route('/temp')
# def get_info():
#
#     player = {
#        'name': 'Messi',
#        'nation': 'Argentina',
#        'age': 35,
#         'club': 'Barcelona'
#     }
#     ret = render_template('login.html', player=player)
#     return ret


print('=' * 30)
print(app.url_map)
print(app.root_path)
print(app.static_folder)
# print(app.static_url_path)
print(app.template_folder)
print(app.jinja_loader.searchpath)
print('=' * 30)
