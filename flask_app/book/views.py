# encoding: utf-8
"""
@version: 1.0
@author: Jarrett
@file: views
@time: 2021/11/10 16:01
"""
from flask_restful import Resource, reqparse, Api
from flask_app.common.utils import BaseResponse
from flask_app.user import user_blueprint
from .models import db, BookModel

api = Api(user_blueprint)

REQUIRED_INFO = "该参数是必须的！"

class BookView(Resource):
    def get(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass


class BookListView(Resource):
    def post(self):
        pass

    def post(self):
        pass


api.add_resource(BookView, "/book")
api.add_resource(BookListView, "/bookList")