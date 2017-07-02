from app import db

class User(db.Model):
    __tablename__ = "usernames"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    tweet_data = db.relationship('TweetData', backref='author', lazy='dynamic')

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<Username %r>' % self.username

class TweetData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
