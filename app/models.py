from .extensions import db

class VideoGame(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  year = db.Column(db.Integer, nullable=False)
  image_url = db.Column(db.String(1024), nullable=False)

  def __init__(self, title, year, image_url):
    self.title = title
    self.year = year
    self.image_url = image_url