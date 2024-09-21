# Import the Flask class from the Flask library

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# Create a new Flask application instance and store it in the 'app' variable

app = Flask(__name__)
app.config["SECRET_KEY"] = "3b3ef996c15f28295621be10aa478769"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
from app_04 import routes
