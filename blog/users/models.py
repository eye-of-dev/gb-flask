from flask_login import UserMixin
from werkzeug.security import check_password_hash

from blog.database import db


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(255))
    is_staff = db.Column(db.SmallInteger(), default=0)

    def __init__(self, email, password_hash, name):
        self.email = email
        self.password_hash = password_hash
        self.name = name

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
