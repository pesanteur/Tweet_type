from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.heroku import Heroku

app = Flask(__name__)

heroku = Heroku(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views
