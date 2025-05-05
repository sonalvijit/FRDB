from flask import Blueprint, jsonify, request
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from models import User, db, Tweet, LikeTweet, Comment, LikeComment, Followers
from handler import handle_register, handle_login, handle_create_tweet, handle_view_profile, handle_like_tweet, handle_fetch_tweet, handle_create_comment, handle_like_comment, handle_follow_user, handle_unfollow_user, handle_view_followers, handle_view_followings, handle_index, handle_restricted_area

routes_bp = Blueprint("routes_bp", __name__)
login_manager = LoginManager()

@login_manager.unauthorized_handler
def unauthorized():
     return jsonify({"error":"Unauthorized Access!"}), 400

@login_manager.user_loader
def user_loader(user_id):
     return User.query.get(int(user_id))

@routes_bp.route("/")
def index_page():
     return handle_index()

@routes_bp.route("/register", methods=["POST"])
def register():
     data = request.json
     return handle_register(User=User, db=db, data=data)

@routes_bp.route("/login", methods=["POST"])
def login_user():
     data = request.json
     return handle_login(User=User, data=data)

@routes_bp.route("/profile/<string:username>",methods=["GET"])
def view_profile(username):
     return handle_view_profile(User=User, username=username)

@routes_bp.route("/restricted")
@login_required
def restricted_area():
     return handle_restricted_area()

@routes_bp.route("/create_tweet",methods=["POST"])
@login_required
def create_tweet():
     data = request.json
     return handle_create_tweet(Tweet=Tweet, user_id=current_user.id, data=data, db=db)

@routes_bp.route("/like",methods=["POST"])
@login_required
def like_tweet():
     tweet_id_ = request.args.get("tweet_id")
     return handle_like_tweet(LikeTweet=LikeTweet, tweet_id=tweet_id_, current_user=current_user.id ,db=db)

@routes_bp.route("/tweet",methods=["GET"])
@login_required
def view_tweet():
     return handle_fetch_tweet(Tweet=Tweet, LikeTweet=LikeTweet)

@routes_bp.route("/create_comment/<int:tweet_id>",methods=["POST"])
@login_required
def create_comment(tweet_id):
     data = request.json
     return handle_create_comment(Comment=Comment, user_id=current_user.id, tweet_id=tweet_id, data=data, db=db)

@routes_bp.route("/like",methods=["POST"])
@login_required
def like_comment():
     comment_id = int(request.args.get("comment_id"))
     return handle_like_comment(LikeComment=LikeComment, comment_id=comment_id, current_user=current_user.id, db=db)

@routes_bp.route("/follow", methods=["POST"])
@login_required
def follow_user():
     username = request.args.get("username")
     return handle_follow_user(username=username, User=User, current_user=current_user.id, Followers=Followers, db=db)

@routes_bp.route("/unfollow", methods=["POST"])
@login_required
def unfollow_user():
     username = request.args.get("username")
     return handle_unfollow_user(username=username, User=User, current_user=current_user.id, Followers=Followers, db=db)

@routes_bp.route("/followers",methods=["POST"])
@login_required
def get_followers():
     username = request.args.get("username")
     return handle_view_followers(User=User, username=username)

@routes_bp.route("/following", methods=["GET"])
@login_required
def get_following():
     username = request.args.get("username")
     return handle_view_followings(User=User, username=username)