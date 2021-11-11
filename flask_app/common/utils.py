# encoding: utf-8
"""
@version: 1.0
@author: Jarrett
@file: utils
@time: 2021/11/10 16:02
"""
from flask import jsonify
from flask_app import app

class BaseResponse:
    def __init__(self):
        self.result_code_success = 200
        self.result_code_fail = 201

    def success(self, msg="success", data={}):
        result = {
            "code": self.result_code_success,
            "message": msg,
            "data": data
        }
        return jsonify(result)

    def fail(self, msg="fail", data={}):
        result = {
            "code": self.result_code_fail,
            "message": msg,
            "data": data
        }
        return jsonify(result)

def test():
    with app.app_context():
        a = BaseResponse()
        print(a.success())


if __name__ == "__main__":
    test()