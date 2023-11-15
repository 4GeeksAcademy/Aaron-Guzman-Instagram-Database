import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)  
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(Integer)
    location = Column(String(250))
    birthday = Column(String(10), nullable=False)
    facebook_account = Column(String(30))
    followers = Column(String(30), nullable=False)
    posts = relationship("Post")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    date = Column(String(250))
    location = Column(String(250))
    like = Column(String(250), nullable=False)
    description = Column(String(250), ForeignKey('user.id'))
    user = relationship("User", back_populates="posts")

class Update(Base):
    __tablename__ = 'update'
    id = Column(Integer, primary_key=True)
    date = Column(String(250))
    viewer = Column(String(250))
    reaction = Column(String(250), nullable=False)
    description = Column(String(250), ForeignKey('user.id'))
    user = relationship("User", back_populates="updates")

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    reaction = Column(String(5))
    date = Column(String(250), nullable=False)
   


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
