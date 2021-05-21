from flask import Flask

from blog.articles.views import articles
from blog.auth.views import auth, login_manager
from blog.database import db
from blog.users.views import users


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'o)^xsrh#7(7&n1r+62!vz*qp+ih=lhem5_i%j_#o7wu-5&7#y*'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    login_manager.init_app(app)

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users)
    app.register_blueprint(articles)
    app.register_blueprint(auth)
