# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from werkzeug.exceptions import HTTPException

from app.app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()


# 全局异常捕获
@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg=msg, code=code, error_code=error_code)
    else:
        # flag = app.config['DEBUG']
        # print(flag)
        if app.config['DEBUG']:
            return e
        else:
            return ServerError()


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])