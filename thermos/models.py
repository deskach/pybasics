from datetime import datetime
from sqlalchemy import desc

from thermos import db 

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow) 
    # ^ here we pass a function not value because we want to make a call to the function every time
    #   a new bookmark object is created. Otherwise same value would have been used what we do not want.
    description = db.Column(db.String(300))

    @staticmethod
    def new_bookmarks(num):
        return Bookmark.query.order_by(desc(Bookmark.date)).limit(num)

    def __repr__(self):
        return "<Bookmark '{}': '{}'>".format(self.description, self.url)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return "<User '{}'>".format(self.username)
