from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

from blog.users.models import Users

users = Blueprint('users', __name__, url_prefix='/users', static_folder='../static')


@users.route('/')
def users_list():
    users = Users.query.all()
    return render_template(
        'users/list.html',
        users=users
    )


@users.route('/<int:pk>/')
@login_required
def users_info(pk: int):
    user = Users.query.filter_by(id=pk).one_or_none()

    if user is None:
        raise NotFound(f'User #{pk} does not exist!')

    return render_template(
        'users/detail.html',
        user=user
    )
