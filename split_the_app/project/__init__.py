from flask import Flask
from flask_sqlalchemy import SQLAlchemy # install this first!

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///side.db'
db = SQLAlchemy(app)


app = Flask(__name__)