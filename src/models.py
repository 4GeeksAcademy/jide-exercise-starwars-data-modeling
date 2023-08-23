import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
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
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    loginStatus = Column(String(250), nullable=False)
    favorites_id = Column(Integer, ForeignKey("favorites.id"), nullable=True)
    # registerDate = Column(Date)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table characters.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    gender = Column(String(250))
    hairColor = Column(String(250))
    eyeColor = Column(String(250))
    favorites = relationship('Favorites', backref='characters', lazy=True)
    
class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table planets.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    terrain = Column(String(250))
    climate = Column(String(250))
    favorites = relationship('Favorites', backref='planets', lazy=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table vehicles.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    crew = Column(Integer)
    favorites = relationship('Favorites', backref='vehicles', lazy=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey("characters.id"), nullable=True)
    planets_id = Column(Integer, ForeignKey("planets.id"), nullable=True)
    vehicles_id = Column(Integer, ForeignKey("vehicles.id"), nullable=True)
    user = relationship('User', backref='favorites', lazy=True, uselist=False)


  

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
