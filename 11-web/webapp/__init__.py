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
import books

app = Flask('webapp')
app.register_blueprint(books.book)


# 默认是Get请求，还有HEAD OPTIONS
# flask中只要处理返回的内容，可以编写返回码，如果需要添加header也可以
@app.route('/')
@app.route('/index', methods=['post'])
def index():
    # return 'abc'
    res = Response('abc', status=201)
    res.headers.add_header('X-Study', 'Java')
    return res


@app.route('/json', methods=['Get', 'Post'])
def get_json():
    res = {
        'count': 3,
        'result': [
            (1, 'Pablo', 20),
            (2, 'Fernando', 30),
            (3, 'Bob', 35)
        ]
    }
    # return Response(json.dumps(res), content_type='application/json')
    res = jsonify(res)
    res.status = 201
    return res


@app.route('/temp')
def get_info():

    player = {
       'name': 'Messi',
       'nation': 'Argentina',
       'age': 35,
        'club': 'Barcelona'
    }
    ret = render_template('index.html', player=player)
    return ret


print('=' * 30)
print(app.url_map)
print(app.root_path)
print(app.static_folder)
print(app.static_url_path)
print(app.template_folder)
print(app.jinja_loader.searchpath)
print('=' * 30)
