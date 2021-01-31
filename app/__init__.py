from flask import Flask
import os
from .extensions import db
from .views import main

def create_app():
  app = Flask(__name__)
  app.register_blueprint(main)
  app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DB_URI')
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ.get('TRACK_MODIFICATIONS')

  db.init_app(app)

  return app