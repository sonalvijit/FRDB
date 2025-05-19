from run import login_user
from json import load
from requests import Session
from os import path, remove, getenv
from dotenv import load_dotenv

load_dotenv()
ptr_ = getenv("PORT")
base_url:str = f"http://localhost:{ptr_}"

def follower_user():
     if not path.isfile("./cookie.json"):
          login_user()
          with open("./cookie.json", "r") as f:
               cookies = load(f)
               session = Session()
               session.cookies.update(cookies)
               create_twt = f"{base_url}/follow"
               response = session.post(create_twt, json={
                    "username":"itravis"
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
               create_twt = f"{base_url}/follow"
               response = session.post(create_twt, json={
                    "username":"itravis"
               })
               if response.status_code == 201:
                    print("Comment Created:", response.json())
               else:
                    print("Not Logged in or session expired:", response.status_code, response.text)
          remove("./cookie.json")

if __name__ == "__main__":
     [follower_user() for _ in range(1500)]