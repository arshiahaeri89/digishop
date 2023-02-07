from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

fileDir = os.path.dirname(os.path.abspath(__file__))

goalRoute = os.path.join(fileDir, 'app.db')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + goalRoute


db = SQLAlchemy(app)

import shop.views
import shop.models
