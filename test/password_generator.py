from string import digits, ascii_uppercase, ascii_lowercase
from random import choice

sre_ = digits + ascii_lowercase + ascii_uppercase
lsre = list(sre_)

def get_pwd():
     wrd_:str = ""
     for _ in range(30):
          a = choice(lsre)
          wrd_=wrd_+a
     return wrd_