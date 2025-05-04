from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from os import path

Base = declarative_base()

class User(Base):
     __tablename__ = "users"
     id = Column(Integer, primary_key=True)
     username = Column(String, unique=True, nullable=False)
     email = Column(String, unique=True, nullable=False)
     password = Column(String, nullable=False)

DATABASE_URI = "sqlite:///user_info.db"
engine = create_engine(DATABASE_URI, echo=False)

Session = sessionmaker(bind=engine)

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
     print(f"User: {username} added!")
     session.close()