from flask import Blueprint, render_template, redirect

users = Blueprint('users', __name__, url_prefix='/users', static_folder='../static')

USERS = {
    1: 'Романов Денис Игоревич',
    2: 'Семенов Кирилл Андреевич',
    3: 'Матвеев Максим Филиппович',
    4: 'Орлов Марсель Максимович',
    5: 'Масленникова Екатерина Ивановна',
}


@users.route('/')
def users_list():
    return render_template(
        'users/list.html',
        users=USERS
    )


@users.route('/<int:pk>/')
def users_info(pk: int):

    try:
        user = USERS[pk]
    except KeyError:
        return redirect('/users/')

    return render_template(
        'users/detail.html',
        user=user
    )
