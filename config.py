
import os

# Your App secret key
SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

basedir = os.path.abspath(os.path.dirname(__file__))
# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False