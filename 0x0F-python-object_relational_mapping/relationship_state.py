#!/usr/bin/python3
"""Defines a state model"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """It represent the states table"""
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
