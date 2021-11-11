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
from .models import db, UserModel

api = Api(user_blueprint)

REQUIRED_INFO = "该参数是必须的！"

def row2dict(row):
    """
    参考文档 https://stackoverflow.com/questions/1958219/convert-sqlalchemy-row-object-to-python-dict
    将model转换为dict
    :param row: Sqlalchemy model
    :return: 输出的字典
    """
    out_dict = {}
    for column in row.__table__.columns:
        out_dict[column.name] = str(getattr(row, column.name))
    return out_dict

class UserView(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, help=REQUIRED_INFO)
        args = parser.parse_args()
        _user_id = args.get("id")
        user = UserModel.query.get(_user_id)
        if user:
            user_dict = row2dict(user)
            return BaseResponse().success(data=user_dict)
        else:
            return BaseResponse().fail()

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, help=REQUIRED_INFO)
        args = parser.parse_args()
        _user_id = args.get("id")
        user = UserModel.query.get(_user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return BaseResponse().success()
        else:
            return BaseResponse().fail()

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, location="json", help=REQUIRED_INFO)
        parser.add_argument("username", location="json")
        parser.add_argument("age", location="json")
        parser.add_argument("sex", location="json")
        args = parser.parse_args()
        _user_id = args.get("id")
        # 从参数中剔除id这个键值
        del args["id"]
        user = UserModel.query.get(_user_id)
        if user:
            UserModel.query.filter(UserModel.id == _user_id).update(args)
            db.session.commit()
            return BaseResponse().success()
        else:
            return BaseResponse().fail()


class UserListView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, location="json", help=REQUIRED_INFO)
        parser.add_argument("age", location="json")
        parser.add_argument("sex", location="json")
        args = parser.parse_args()
        user = UserModel(username=args.get("username"),
                         age=args.get("age"),
                         sex=args.get("sex"))
        db.session.add(user)
        db.session.commit()
        return BaseResponse().success(data=row2dict(user))

    def get(self):
        user_list = UserModel.query.all()
        _user_list = []
        for user in user_list:
            _user_list.append(row2dict(user))
        return BaseResponse().success(data=_user_list)


api.add_resource(UserView, "/user")
api.add_resource(UserListView, "/userList")
