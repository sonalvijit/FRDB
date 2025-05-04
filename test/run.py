from faker import Faker
from dotenv import load_dotenv
from os import getenv
from requests import get, post
from password_generator import get_pwd
from user_info_db import initialize_db, add_user_info

load_dotenv()
ptr_ = getenv("PORT")
base_url:str = f"http://localhost:{ptr_}"

initialize_db()

get_data_ = Faker()

def register_user():
     username = get_data_.user_name()
     email = get_data_.email()
     pwd = get_pwd()
     a = post(f"{base_url}/register", json={
          "username":username,
          "email":email,
          "password":pwd
     })
     print(f"{username} was created")
     add_user_info(username=username, email=email, password=pwd)
     return [username, email, pwd]

[register_user() for _ in range(120)]