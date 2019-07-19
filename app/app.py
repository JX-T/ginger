# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncode


class JSONEncoder(_JSONEncode):
    def default(self, o):
        if hasattr(o, '__getitem__') and hasattr(o, 'keys'):
            # dict函数，创建一个字典对象，一般用法：dict(name='tom', age='18')
            # 如何将一个对象的属性转换成字典，obj.__dict__ 只会返回对象实例的实例属性, 无法返回对应的类属性
            # 如何有效的将对象转换成字典，在对象的类中 实现 keys 和 __getitem__ 方法就可以了
            return dict(o)


class Flask(_Flask):
    # 使用自定义的JSONEncoder替换Flask自带的JSONEncode
    json_encoder = JSONEncoder



