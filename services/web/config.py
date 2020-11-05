import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/project/media"

    # APP MODE
    DEBUG = False

    # Top secret of website
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # # Database configuration
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'project.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Bootstrap using local static files
    BOOTSTRAP_SERVE_LOCAL = True

    # Mail Configuration
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'kfu.anatomy.2018@gmail.com'
    MAIL_PASSWORD = 'D97cfg845dcv'

    # ADMINS
    ADMINS = ['kfu.anatomy.2018@gmail.com']
    ADMINS_PWD = [os.getenv('ADMIN_PWD')]

    # LOCAL
    LOCAL = False
    API_URL = 'localhost:5000' if LOCAL else 'web:1000'
