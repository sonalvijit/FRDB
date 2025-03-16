from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(50), nullable=False)
     email = db.Column(db.String(256), nullable=False)
     password = db.Column(db.String(288), nullable=False)
     date_created = db.Column(db.Integer, default=datetime.utcnow().fromtimestamp())

     tweets = db.relationship('tweet', lazy=True, cascade="all, delete")
     comments = db.relationship('comment', lazy=True, cascade="all, delete")
     like_comments = db.relationship('likecomment', lazy=True, cascade="all, delete")
     like_tweets = db.relationship('liketweet', lazy=True, cascade="all, delete")
     @classmethod
     def set_password(self, pwd):
          self.password = generate_password_hash(pwd)

     @classmethod
     def check_hash(self, pwd):
          return check_password_hash(self.password, pwd)

class Tweet(db.Model):
     __tablename__ = "tweet"

     id = db.Column(db.Integer, primary_key=True)
     tweet = db.Column(db.Text, nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     date_created = db.Column(db.Integer, default=datetime.utcnow().fromtimestamp())

     comments = db.relationship("comment", lazy=True, cascade="all, delete")
     liked_tweet = db.relationship('liketweet', lazy=True, cascade="all, delete")

class Comment(db.Model):
     __tablename__= "comment"

     id = db.Column(db.Integer, primary_key=True)
     comment = db.Column(db.Text, nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     tweet_id = db.Column(db.Integer, db.ForeignKey('tweet.id'))
     date_created = db.Column(db.Integer, default=datetime.utcnow().fromtimestamp())

     comments_likes = db.relationship("likecomment", lazy=True, cascade="all, delete")

class LikeComment(db.Model):
     __tablename__ = "likecomment"

     id = db.Column(db.Integer, primary_key=True)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))

class LikeTweet(db.Model):
     __tablename__= "liketweet"

     id = db.Column(db.Integer, primary_key=True)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     tweet_id = db.Column(db.Integer, db.ForeignKey('tweet'))
