from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(50), unique=True, nullable=False)
     email = db.Column(db.String(256),  unique=True, nullable=False)
     password = db.Column(db.String(288), nullable=False)
     date_created = db.Column(db.Integer, default=db.func.strftime('%s', 'now'))

     tweets = db.relationship('Tweet', backref="author", lazy=True, cascade="all, delete")
     comments = db.relationship('Comment', lazy=True, cascade="all, delete")
     like_comments = db.relationship('LikeComment', lazy=True, cascade="all, delete")
     like_tweets = db.relationship('LikeTweet', lazy=True, cascade="all, delete")

     def check_hash(self, pwd):
          return check_password_hash(self.password, pwd)

class Tweet(db.Model):
     __tablename__ = "tweet"

     id = db.Column(db.Integer, primary_key=True)
     tweet = db.Column(db.Text, nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     date_created = db.Column(db.Integer, default=db.func.strftime('%s', 'now'))

     comments = db.relationship("Comment", lazy=True, cascade="all, delete")
     liked_tweet = db.relationship('LikeTweet', lazy=True, cascade="all, delete")

class Comment(db.Model):
     __tablename__= "comment"

     id = db.Column(db.Integer, primary_key=True)
     comment = db.Column(db.Text, nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     tweet_id = db.Column(db.Integer, db.ForeignKey('tweet.id'))
     date_created = db.Column(db.Integer, default=db.func.strftime('%s', 'now'))

     comments_likes = db.relationship("LikeComment", lazy=True, cascade="all, delete")

class LikeComment(db.Model):
     __tablename__ = "likecomment"

     id = db.Column(db.Integer, primary_key=True)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))

class LikeTweet(db.Model):
     __tablename__= "liketweet"

     id = db.Column(db.Integer, primary_key=True)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     tweet_id = db.Column(db.Integer, db.ForeignKey('tweet.id'))

class Followers(db.Model):
     __tablename__ = "followers"

     id = db.Column(db.Integer, primary_key=True)
     follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
     followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
     created_at = db.Column(db.Integer, default=db.func.strftime('%s', 'now'))

     follower = db.relationship('User', foreign_keys=[follower_id], backref=db.backref('following', lazy='dynamic'))
     followed = db.relationship('User', foreign_keys=[followed_id], backref=db.backref('followers', lazy='dynamic'))

     def __repr__(self):
          return f"<Follower {self.follower_id} follows {self.followed_id}>"
