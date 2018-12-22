from flask_sqlalchemy_test import db
# 将要创建表的模型所属文件导入
from flask_sqlalchemy_test.models import user

db.drop_all()
db.create_all()
