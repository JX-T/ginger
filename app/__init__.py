# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from app.app import Flask


def register_blueprints(f_app):
    from app.api.v1 import create_blueprint_v1
    f_app.register_blueprint(create_blueprint_v1())


def register_plugin(d_app):
    from app.models.base import db
    db.init_app(app=d_app)
    with d_app.app_context():
        db.create_all(app=d_app)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    register_blueprints(app)
    register_plugin(app)

    return app