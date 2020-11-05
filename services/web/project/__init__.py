from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_migrate import Migrate
from flask_socketio import SocketIO

from config import Config

bcrypt = Bcrypt()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
mail = Mail()
bootstrap = Bootstrap()
socketio = SocketIO()


def create_app(config=Config):
    app = Flask(__name__, static_url_path='')
    app.config.from_object(config)
    app.config['URL'] = 'localhost:5000' if app.config['LOCAL'] else 'api:1000'

    bcrypt.init_app(app)
    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)
    bootstrap.init_app(app)
    socketio.init_app(app)

    from project.main.routes import main
    app.register_blueprint(main)

    from project.auth.routes import auth
    app.register_blueprint(auth)

    from project.api.routes import api
    app.register_blueprint(api)

    return app

from project import model
