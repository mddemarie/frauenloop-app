from flask import Flask
from flask_sqlalchemy import SQLAlchemy # install this first!

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///side.db' # with pg_admin you can acces tables
db = SQLAlchemy(app)

app = Flask(__name__)

from project import controllers