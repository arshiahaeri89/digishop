from flask import Flask
import os

app = Flask(__name__)

goalRoute = os.path.join(fileDir, 'app.db')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + goalRoute

db = SQLAlchemy(app)

import weblog.views
import weblog.models
