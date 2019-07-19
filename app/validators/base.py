# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):

    def __init__(self, formdata=None, obj=None, prefix='', data=None, meta=None, **kwargs):
        # data = request.json
        super(BaseForm, self).__init__(formdata=formdata, obj=obj, prefix=prefix, data=data, meta=meta, **kwargs)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
