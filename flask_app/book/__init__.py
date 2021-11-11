# encoding: utf-8
"""
@version: 1.0
@author: Jarrett
@file: __init__.py
@time: 2021/11/10 15:50
"""
from flask import Blueprint

book_blueprint = Blueprint("book_blueprint", __name__, url_prefix="/book")
from flask_app.book import views