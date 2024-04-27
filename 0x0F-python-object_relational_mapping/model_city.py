#!/usr/bin/python3
""" Defining the City class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = declarative_base()


class City(Base):
    """
    City class that iherits from the Base class
    Attributes: id (Int)
                name (Str)
                state_id (str)
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
