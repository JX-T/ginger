# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from contextlib import contextmanager

from sqlalchemy import Column, Integer, SmallInteger

from app.libs.error_code import NotFound


class SQLALchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    # 为了保持异常格式的一致性，重写 get_or_404 和 first_or_404 函数
    def get_or_404(self, ident):
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    def first_or_404(self):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv


db = SQLALchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column(Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    # 实现 此函数，就可以使用对象+[]的方式，也就是说当对象使用 sef[item] 时就会调用此函数，并将item作为参数传入
    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    # def delete(self):
    #     self.status = 0
    #
    # def append(self, *keys):
    #     for key in keys:
    #         self.fields.append(key)
    #     return self
    #
    # def hide(self, *keys):
    #     for key in keys:
    #         self.fields.remove(key)
    #     return self
    #
    # def keys(self):
    #     return self.fields
