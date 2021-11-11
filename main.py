# encoding: utf-8
"""
@version: 1.0
@author: Jarrett
@file: main
@time: 2021/11/10 16:29
"""
from flask_app import app, db

def init_db():
    # 丢掉全部表
    db.drop_all()
    # 创建全部表
    db.create_all()


if __name__ == "__main__":
    # init_db()
    app.run(debug=True)