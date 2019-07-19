# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from flask import request, current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import UserEmailForm, ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = Redprint('/token', url_prefix='/token')


@api.route('/', methods=['POST'])
def get_token():
    # 参数验证
    form = ClientForm(data=request.json).validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify,
    }
    # 账号，密码验证
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    # 生成 token
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'], form.type.data, scope=None, expiration=expiration)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })

