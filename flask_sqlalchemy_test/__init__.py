from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("settings.py")

db = SQLAlchemy(app)

# 注册蓝图
from .views.user import usr

app.register_blueprint(usr)
