import os
import uuid

basedir = os.path.abspath(os.path.dirname(__file__))

DB_USER = 'fu'
DB_PASSWORD = 'bar'
DB_HOST = 'localhost'
DB_NAME = 'development'
SQLALCHEMY_DATABASE_URI = "mysql://{0}:{1}@{2}/{3}".\
    format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WTF_CSRF_ENABLED = True
SECRET_KEY = str(uuid.uuid4())
