# -*- coding: utf-8 -*-
# __author__ = 'Miracle'


class Tag:
    name = 'tom'
    age = 18

    def __init__(self):
        self.item = {'python': 'This is python'}

    def keys(self):
        return ['name']

    def __getitem__(self, key):
        return getattr(self, key)
    #     print('这个方法被调用')
    #     return self.item[key]


a = Tag()
# print(a['name'])


# d = dict(name='tom', age=18)
d = dict(a)
print(d)


# def arg_test(message):
#     print(message)
#
# arg = "msg"
#
# arg_test(arg)
