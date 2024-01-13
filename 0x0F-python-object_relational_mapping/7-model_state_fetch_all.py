#!/usr/bin/python3
""" A script that lists all State objects 
from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3], pool_pre_ping=True))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(state.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
