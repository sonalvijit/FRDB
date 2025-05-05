from faker import Faker
from dotenv import load_dotenv
from os import getenv
from requests import get, Session, post
from password_generator import get_pwd
from user_info_db import initialize_db, add_user_info, get_user_random
from json import dump, load
from os import path, remove

load_dotenv()
ptr_ = getenv("PORT")
base_url:str = f"http://localhost:{ptr_}"

initialize_db()

get_data_ = Faker()

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
          print("Login in")
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
                    "tweet_id":1
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
                    "tweet_id":3
               })
               if response.status_code == 201:
                    print("Tweet Created:", response.json())
               else:
                    print("Not Logged in or session expired:", response.status_code, response.text)
          remove("./cookie.json")

def generator_user_():
     [register_user(i) for i in range(203)]

generator_user_()
[create_tweet() for _ in range(45)]
[like_tweet_() for _ in range(45)]