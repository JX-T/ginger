# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client', url_prefix='/client')


@api.route('/register/', methods=['POST'])
def create_client():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email,
            ClientTypeEnum.USER_MOBILE: __register_user_by_mobile
        }
        promise[form.type.data]()
        return 'success'
    else:
        raise ClientTypeError()
    # return 'false'


def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
    else:
        print(form.errors)


def __register_user_by_mobile():
    pass

