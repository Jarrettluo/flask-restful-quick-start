# encoding: utf-8
"""
@version: 1.0
@author: Jarrett
@file: models
@time: 2021/11/10 16:01
"""
from datetime import datetime

from flask_app import db

"""
sqlalchemy 参考文档： http://www.pythondoc.com/flask-sqlalchemy/models.html

"""

class UserModel(db.Model):
    # 定义表名
    __tablename__ = "user"
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 姓名，非空且不可重复
    username = db.Column(db.String(64), unique=True, nullable=False)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(4))
    avater = db.Column(db.String(64))
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 更新时间
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)



"""
primary_key：True设置某个字段为主键。
autoincrement：True设置这个字段为自动增长的。
default：设置某个字段的默认值。在发表时间这些字段上面经常用。
nullable：指定某个字段是否为空。默认值是True，就是可以为空。
unique：指定某个字段的值是否唯一。默认是False。
onupdate：在数据更新的时候会调用这个参数指定的值或者函数。在第一次插入这条数据的时候，不会用onupdate的值，只会使用default的值。常用于是update_time字段（每次更新数据的时候都要更新该字段值）。
name：指定ORM模型中某个属性映射到表中的字段名。如果不指定，那么会使用这个属性的名字来作为字段名。如果指定了，就会使用指定的这个值作为表字段名。这个参数也可以当作位置参数，在第1个参数来指定。
"""