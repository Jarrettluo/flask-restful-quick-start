# encoding: utf-8
"""
@version: 1.0
@author: Jarrett
@file: __init__.py
@time: 2021/11/10 15:49
"""
from flask import Blueprint

user_blueprint = Blueprint("user_blueprint", __name__, url_prefix="/user")
from flask_app.user import views
