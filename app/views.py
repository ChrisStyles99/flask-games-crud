from flask import Blueprint
from .models import VideoGame

main = Blueprint('main', __name__)

@main.route('/')
def index():
  video_games = VideoGame.query.all()
  print(video_games)
  return 'Home'
