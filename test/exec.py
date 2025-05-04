from faker import Faker
from dotenv import load_dotenv
from os import getenv
from requests import get

load_dotenv()
ptr_ = getenv("PORT")
base_url:str = f"http://localhost:{ptr_}"


a = get(base_url)
if a.status_code == 200:
     print("OK")