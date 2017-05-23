import os

from flask import Flask, render_template, request, redirect  # etc.
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

# Create and name Flask app
app = Flask("FlaskLoginApp")

# ?ssl=false&replicaSet=cluster1-shard-0&authSource=admin


# database connection

# _MONGODB_USER = 'sumit18494'
# _MONGODB_PASSWD = '3PceiozJTa9QCpQY'
# _MONGODB_HOST = 'cluster1-shard-00-00-d9hyh.mongodb.net:27017,cluster1-shard-00-01-d9hyh.mongodb.net:27017,cluster1-shard-00-02-d9hyh.mongodb.net:27017'
# _MONGODB_NAME = 'productevaluation'
# _MONGODB_DATABASE_HOST = \
#     'mongodb://%s:%s@%s/%s?ssl=true&replicaSet=cluster1-shard-0&authSource=admin' \
#     % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)
# _MONGODB_ALIAS = 'productevaluation'


_MONGODB_NAME = 'pes'
_MONGODB_DATABASE_HOST = "localhost"
app.config['MONGODB_SETTINGS'] = {'db': _MONGODB_NAME,'host' : _MONGODB_DATABASE_HOST}
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "someSecret")
app.debug = os.environ.get('DEBUG', True)

db = MongoEngine(app) # connect MongoEngine with Flask App
# db.init_app(app)
app.session_interface = MongoEngineSessionInterface(db) # sessions w/ mongoengine

# Flask BCrypt will be used to salt the user password
flask_bcrypt = Bcrypt(app)

# Associate Flask-Login manager with current app
login_manager = LoginManager()
login_manager.init_app(app)
