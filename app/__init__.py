from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

def create_app():
	app = Flask(__name__)

	app.config.from_object('config')
	return app

app = create_app()
app.secret_key = "super secret key"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app.controllers import *
from app.functions import *
from app.api_helper import *


