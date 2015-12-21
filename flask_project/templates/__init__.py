import os

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from factory import AppFactory
from settings import DevelopmentConfig,\
    TestConfig, ProductionConfig

configs = {'development': DevelopmentConfig,
           'test': TestConfig,
           'prod': ProductionConfig,
}

config = configs[os.environ.get("ENV", "development")]
app = AppFactory(config=config, name=__name__).get_app()
#lm = LoginManager()
#lm.init_app(app)
#lm.login_view = 'login'
db = SQLAlchemy(app)
