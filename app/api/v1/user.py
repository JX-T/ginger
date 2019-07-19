# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from flask import g, jsonify

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

api = Redprint('user', url_prefix='/user')


@api.route('/', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    # 使用 jsonify 序列化 python 对象时，如果对象无法序列化，会调用 flask.json.JSONEncoder 类的 default 函数来处理无法序列化的对象
    # 在 default 函数中将无法序列化的对象转换成可以序列化的对象
    return jsonify(user)

