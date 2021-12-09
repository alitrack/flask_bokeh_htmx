
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# import os
# import jinja_partials
app = Flask(__name__)
app.config.from_object("config")
# db = SQLAlchemy(app)


# jinja_partials.register_extensions(app)

from . import views

    