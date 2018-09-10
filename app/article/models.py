from app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    date = db.TIMESTAMP()
    views = db.Column(db.Integer)
