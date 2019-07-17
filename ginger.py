# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from app.app import create_app

app = create_app()


@app.route('/get')
def get_user():
    return ''


if __name__ == '__main__':
    app.run(debug=True)