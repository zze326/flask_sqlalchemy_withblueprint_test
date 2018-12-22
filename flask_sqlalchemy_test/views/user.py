from flask import Blueprint, render_template
from flask_sqlalchemy_test.models import user
from flask_sqlalchemy_test import db

# 实例化
usr = Blueprint('usr', __name__, url_prefix='/user')


@usr.route('/list')
def list():
    user_list = db.session.query(user.User.id, user.User.name).all()
    return render_template('list.html', list=user_list)
