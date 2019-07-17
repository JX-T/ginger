# -*- coding: utf-8 -*-
# __author__ = 'Miracle'


from app.libs.redprint import Redprint

api = Redprint('user', url_prefix='/user')


@api.route('/get/', methods=['GET'])
def get_user():
    return 'user'

