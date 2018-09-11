from app import db
from datetime import *


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    date = db.Column(db.TIMESTAMP)
    views = db.Column(db.Integer)
    ip = db.Column(db.String(20))
    # 무엇의 답글? 원글이면 아이디와 동일, 특정 글의 답글이면 그거 써져야함.
    gnum = db.Column(db.Integer, nullable=True)
    # 몇번째 답글?
    onum = db.Column(db.Integer)
    # 들여쓰기.
    nested = db.Column(db.Integer)

    def __init__(self, title, author, ip, gnum=None, onum=0, nested=0):
        self.title = title
        self.author = author
        self.date = datetime.utcnow() + timedelta(hours=9)
        self.views = 0
        self.ip = ip
        if gnum:
            self.gnum = gnum
        self.onum = onum
        self.nested = nested

    def __repr__(self):
        return 'article {}'.format(self.title)
