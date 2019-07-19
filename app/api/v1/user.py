# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from flask import g

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

api = Redprint('user', url_prefix='/user')


@api.route('/', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return 'i am Miracle'

