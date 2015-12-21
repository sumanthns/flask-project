import os
import uuid

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DATABASE_QUERY_TIMEOUT = 0.5
    WTF_CSRF_ENABLED = True
    SECRET_KEY = str(uuid.uuid4())
    HOSTNAME = 'localhost'
    DEBUG = True

    URL_MODULES = [
        #'core.urls.routes',
    ]

    BLUEPRINTS = [
        #'core.core',
    ]

    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_PASSWORD_SALT = "secret_password_salt"


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    WTF_CSRF_ENABLED = False
    TESTING = True


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    HOSTNAME = os.environ.get("HOSTNAME")
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT")
