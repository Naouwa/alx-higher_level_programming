#!/usr/bin/python3
""" A file that contains the class definition of a State 
and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """The state class with id and name attributes of each state"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
            nullable=False, unique=True)
    name =  Column(String(128), nullable=False)
