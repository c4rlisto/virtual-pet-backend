#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    bio = Column(Text, nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, userna/home/carl/development/code/phase3/virtual-pet/backend/virtual-pet.db        me='{self.username}', email='{self.email}')>"

class Pets(Base):
    __tablename__ = 'pets'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    species = Column(String(50), nullable=False)
    owner_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Pet(id={self.id}, name='{self.name}', species='{self.species}', owner_id={self.owner_id})>"
    

class Actions(Base):
    __tablename__ = 'actions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    pet_id = Column(Integer, nullable=False)
    action_type = Column(String(50), nullable=False)
    timestamp = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Activity(id={self.id}, pet_id={self.pet_id}, action_type='{self.action_type}', timestamp='{self.timestamp}')>"
    

class tricks(Base):
    __tablename__ = 'tricks'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    pet_id = Column(Integer, nullable=False)
    trick_name = Column(String(50), nullable=False)
    difficulty_level = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Trick(id={self.id}, pet_id={self.pet_id}, trick_name='{self.trick_name}', difficulty_level='{self.difficulty_level}')>"
    
