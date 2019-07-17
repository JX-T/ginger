# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from app.libs.error import APIException


class ClientTypeError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999

