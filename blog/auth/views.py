from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import login_required, logout_user, login_user, LoginManager
from werkzeug.security import generate_password_hash

from blog.auth.models import LoginForm, RegistrationForm
from blog.database import db
from blog.users.models import Users

auth = Blueprint('auth', __name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.filter_by(id=user_id).one_or_none()


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = Users.query.filter_by(email=email).one_or_none()

        if user is None:
            flash(f'Пользователь с таким email {email} не найден')
            return redirect('/login')

        if user and not user.check_password(password=form.password.data):
            flash(f'Неправильный пароль для входа')
            return redirect('/login')

        login_user(user)

        next = request.args.get('next')
        return redirect(next or url_for('users.users_info', pk=user.id))

    return render_template('auth/login.html', form=form)


@auth.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data),
            name=form.name.data
        )

        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('users.users_info', pk=user.id))

    return render_template('auth/registration.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.users_list'))
