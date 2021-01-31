from flask import Blueprint, render_template, request, redirect
from .models import VideoGame
from .extensions import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
  video_games = VideoGame.query.all()
  print(video_games)
  return 'Home'

@main.route('/game/<id>')
def game(id):
  id = int(id)
  video_game = VideoGame.query.get(id)
  return 'Single Game'

@main.route('/add')
def add():
  return 'Add game'

@main.route('/create', methods=["POST"])
def create():
  title = request.form.get('title')
  year = request.form.get('year')
  image_url = request.form.get('image_url')
  year = int(year)
  newGame = VideoGame(title, year, image_url)
  db.session.add(newGame)
  db.session.commit()
  return redirect('/')

@main.route('/delete', methods=["POST"])
def delete():
  game_id = request.form.get('game_id')
  game = VideoGame.query.get(game_id)
  db.session.delete(game)
  db.session.commit()
  return redirect('/')