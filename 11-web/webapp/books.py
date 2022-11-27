from flask import Blueprint, render_template

book = Blueprint('book', __file__, url_prefix='demo')


@book.route('/info')
def get_book():
    pass


print('=' * 30)
print(book.root_path)
print(book.template_folder)
print(book.jinja_loader.searchpath)
print('=' * 30)
