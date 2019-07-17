# -*- coding: utf-8 -*-
# __author__ = 'Miracle'


class Tag:
    def __init__(self):
        self.item = {'python': 'This is python'}

    def __getitem__(self, key):
        print('这个方法被调用')
        return self.item[key]


a = Tag()
print(a['python'])


def arg_test(message=None):
    print(message)

arg = "msg"

arg_test(arg)
