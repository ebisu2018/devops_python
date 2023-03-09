from flask import Blueprint, render_template, jsonify, request

book = Blueprint('book', __name__)


@book.route('/', methods=['Get', 'Post'])
def get_book():
    print(request.content_type)
    print(request.is_json)
    print(request.data)
    print(request.json)
    res = jsonify([
        (1, 'Python'),
        (2, 'Java'),
        (3, 'Golang')
    ])
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Headers'] = 'content-type'
    return res


print('=' * 30)
print(book.root_path)
print(book.template_folder)
print('=' * 30)
