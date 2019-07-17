# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from flask import Flask


def register_blueprints(f_app):
    from app.api.v1 import create_blueprint_v1
    f_app.register_blueprint(create_blueprint_v1())


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    register_blueprints(app)

    return app
