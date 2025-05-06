from faker import Faker
from dotenv import load_dotenv
from os import getenv
from requests import get, Session, post
from password_generator import get_pwd
from user_info_db import initialize_db, add_user_info, get_user_random
from json import dump, load
from os import path, remove
import random

load_dotenv()
ptr_ = getenv("PORT")
base_url:str = f"http://localhost:{ptr_}"

initialize_db()

get_data_ = Faker()

def get_random_integer(upper_limit):
     if upper_limit <= 0:
          raise ValueError("Upper limit must be greater than 0")
     return random.randint(0, upper_limit - 1)

def register_user(i):
     username = get_data_.user_name()
     email = get_data_.email()
     pwd = get_pwd()
     a = post(f"{base_url}/register", json={
          "username":username,
          "email":email,
          "password":pwd
     })
     add_user_info(username=username, email=email, password=pwd)
     print(f"{i}\t\t{username} was created")
     return [username, email, pwd]

def login_user():
     a_ = get_user_random()
     user_name, pass_word = a_[0], a_[1]
     login_env = Session()
     a_ = login_env.post(f"{base_url}/login", json={
          "username":user_name,
          "password":pass_word
     })
     if a_.status_code == 200:
          with open("cookie.json", "w") as f:
               dump(login_env.cookies.get_dict(), f)
     else:
          print("Login Failed")

def create_tweet():
     if not path.isfile("./cookie.json"):
          login_user()
          with open("./cookie.json", "r") as f:
               cookies = load(f)
               session = Session()
               session.cookies.update(cookies)
               create_twt = f"{base_url}/create_tweet"
               text_ = "\n".join(get_data_.paragraph() for _ in range(4))
               response = session.post(create_twt, json={
                    "tweet":text_
               })
               if response.status_code == 201:
                    print("Tweet Created:", response.json())
               else:
                    print("Not Logged in or session expired:", response.status_code, response.text)
          remove("./cookie.json")
     else:
          with open("./cookie.json", "r") as f:
               cookies = load(f)
               session = Session()
               session.cookies.update(cookies)
               create_twt = f"{base_url}/create_tweet"
               text_ = "\n".join(get_data_.paragraph() for _ in range(4))
               response = session.post(create_twt, json={
                    "tweet":text_
               })
               if response.status_code == 201:
                    print("Tweet Created:", response.json())
               else:
                    print("Not Logged in or session expired:", response.status_code, response.text)
          remove("./cookie.json")

def like_tweet_():
     if not path.isfile("./cookie.json"):
          login_user()
          with open("./cookie.json", "r") as f:
               cookies = load(f)
               session = Session()
               session.cookies.update(cookies)
               create_twt = f"{base_url}/like"
               response = session.post(create_twt, json={
                    "tweet_id":get_random_integer(tweet_count)
               })
               if response.status_code == 201:
                    print("Tweet Created:", response.json())
               else:
                    print("Not Logged in or session expired:", response.status_code, response.text)
          remove("./cookie.json")
     else:
          with open("./cookie.json", "r") as f:
               cookies = load(f)
               session = Session()
               session.cookies.update(cookies)
               create_twt = f"{base_url}/like"
               response = session.post(create_twt, json={
                    "tweet_id":get_random_integer(tweet_count)
               })
               if response.status_code == 201:
                    print("Tweet Created:", response.json())
               else:
                    print("Not Logged in or session expired:", response.status_code, response.text)
          remove("./cookie.json")

def like_comment_():
     if not path.isfile("./cookie.json"):
          login_user()
          with open("./cookie.json", "r") as f:
               cookies = load(f)
               session = Session()
               session.cookies.update(cookies)
               create_twt = f"{base_url}/like_comment"
               response = session.post(create_twt, json={
                    "comment_id":get_random_integer(comment_count)
               })
               if response.status_code == 201:
                    print("Liked Comment:", response.json())
               else:
                    print("Not Logged in or session expired:", response.status_code, response.text)
          remove("./cookie.json")
     else:
          with open("./cookie.json", "r") as f:
               cookies = load(f)
               session = Session()
               session.cookies.update(cookies)
               create_twt = f"{base_url}/like_comment"
               response = session.post(create_twt, json={
                    "comment_id":get_random_integer(comment_count)
               })
               if response.status_code == 201:
                    print("Liked Comment:", response.json())
               else:
                    print("Not Logged in or session expired:", response.status_code, response.text)
          remove("./cookie.json")

def create_comment_():
     if not path.isfile("./cookie.json"):
          login_user()
          with open("./cookie.json", "r") as f:
               cookies = load(f)
               session = Session()
               session.cookies.update(cookies)
               create_twt = f"{base_url}/create_comment/{get_random_integer(tweet_count)}"
               comment_ = "\n".join(get_data_.paragraph() for _ in range(4))
               response = session.post(create_twt, json={
                    "comment":comment_
               })
               if response.status_code == 201:
                    print("Comment Created:", response.json())
               else:
                    print("Not Logged in or session expired:", response.status_code, response.text)
          remove("./cookie.json")
     else:
          with open("./cookie.json", "r") as f:
               cookies = load(f)
               session = Session()
               session.cookies.update(cookies)
               create_twt = f"{base_url}/create_comment/{get_random_integer(tweet_count)}"
               comment_ = "\n".join(get_data_.paragraph() for _ in range(4))
               response = session.post(create_twt, json={
                    "comment":comment_
               })
               if response.status_code == 201:
                    print("Comment Created:", response.json())
               else:
                    print("Not Logged in or session expired:", response.status_code, response.text)
          remove("./cookie.json")

def generator_user_():
     [register_user(i) for i in range(50)]

a = get(f"{base_url}/api/tweet_count")
if a.status_code == 200:
     tweet_count = a.json().get("tweet_count")
     print("Tweet Count:", tweet_count)

b = get(f"{base_url}/api/comment_count")
if b.status_code == 200:
     comment_count = b.json().get("comment_count")
     print("Comment Count:", comment_count)

# generator_user_()
# [create_tweet() for _ in range(45)]
# [like_tweet_() for _ in range(45)]
# [create_comment_() for _ in range(45)]
[like_comment_() for _ in range(45)]