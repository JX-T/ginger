# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from app.libs.redprint import Redprint

api = Redprint('book', url_prefix='/book')


@api.route('/search/')
def search():
    return 'book'


