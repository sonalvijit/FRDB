from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from os import path
from random import choice

Base = declarative_base()
DATABASE_URI = "sqlite:///user_info.db"
engine = create_engine(DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine)

class User(Base):
     __tablename__ = "users"
     id = Column(Integer, primary_key=True)
     username = Column(String, unique=True, nullable=False)
     email = Column(String, unique=True, nullable=False)
     password = Column(String, nullable=False)

def initialize_db():
     if path.isdir("user_info.db"):
          print("ALL READY INITIALIZED")
     else:
          Base.metadata.create_all(engine)
          print("CREATE LOCAL DB")

def add_user_info(username, email, password):
     session = Session()

     existing_user_by_username = session.query(User).filter_by(username=username).first()
     if existing_user_by_username:
          print(f"ERROR: Username '{username}' is already taken")
          session.close()
          return
     
     existing_user_by_email = session.query(User).filter_by(email=email).first()
     if existing_user_by_email:
          print(f"ERROR: Email '{email}' is already taken")
          session.close()
          return 
     new_user = User(username=username, email=email, password=password)
     session.add(new_user)
     session.commit()
     session.close()

def get_user_random():
     session = Session()
     users = session.query(User).all()
     if not users:
          print("No users found in the database")
          session.close()
          return
     
     random_user = choice(users)
     session.close()
     return [random_user.username, random_user.password]