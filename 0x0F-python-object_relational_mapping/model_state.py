#!/usr/bin/python3
"""A  file that contains the class definition of a State and
an instance Base = declarative_base():"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model city import city

Base = declarative_base()


class State(Base):
    """The state class with id and name attributes of each state
    __tablename__ (str): The name of the MySQL table to store States
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
