from flask import Flask
from .extensions import db
from .views import main

def create_app(config_file='settings.py'):
  app = Flask(__name__)
  app.config.from_pyfile(config_file)
  app.register_blueprint(main)
  # app.config["SQLALCHEMY_DATABASE_URI"] = config_file.DB_URI
  # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  db.init_app(app)

  return app