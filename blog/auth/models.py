from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from blog.auth.validators import Unique
from blog.users.models import Users


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

    class Meta:
        locales = ['ru_RU']


class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email(), Unique(Users, Users.email)])
    password = PasswordField('Пароль', validators=[DataRequired(),
                                                   EqualTo('confirm_password', message='Пароли должны совпадать')])
    confirm_password = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Submit')

    class Meta:
        locales = ['ru_RU']
