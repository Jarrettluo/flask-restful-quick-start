# encoding: utf-8
"""
@version: 1.0
@author: Jarrett
@file: models
@time: 2021/11/10 16:01
"""
from datetime import datetime
from flask_app import db


class BookModel(db.Model):
    # 定义表名
    __tablename__ = "book"
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(64), unique=True)
    abstact = db.Column(db.String(64))
    image = db.Column(db.String(64))
    uploader_id = db.Column(db.Integer)
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 更新时间
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)
