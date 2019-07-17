# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from flask import Blueprint
from app.api.v1 import user, book, client


def create_blueprint_v1():
    bp = Blueprint('v1', __name__, url_prefix='/v1')
    user.api.register(bp)
    book.api.register(bp)
    client.api.register(bp)
    return bp

