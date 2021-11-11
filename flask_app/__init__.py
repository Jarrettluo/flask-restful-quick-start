# encoding: utf-8
"""
@version: 1.0
@author: Jarrett
@file: __init__.py
@time: 2021/11/10 15:49
"""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# 创建app
app = Flask(__name__)

# 跨域设置
CORS(app, supports_credentials=True)

user = "root"
password = "123456"
database = "flask_quick" # 需要修改的内容
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://%s:%s@localhost:3306/%s" % (user, password, database)

# 设置sqlalchemy自动跟踪数据库
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 查询时显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

# 禁止自动提交数据处理
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

# 注册数据库，创建数据库工具对象
db = SQLAlchemy(app)

from flask_app.user import user_blueprint
from flask_app.book import book_blueprint

app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(book_blueprint, url_prefix="/book")
