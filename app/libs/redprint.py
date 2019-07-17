# -*- coding: utf-8 -*-
# __author__ = 'Miracle'


class Redprint(object):
    def __init__(self, name, url_prefix=''):
        self.name = name
        self.mound = []
        self.url_prefix = url_prefix

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp):
        for f, rule, options in self.mound:
            endpoint = self.name + '_' + options.pop("endpoint", f.__name__)
            bp.add_url_rule(self.url_prefix + rule, endpoint, f, **options)


