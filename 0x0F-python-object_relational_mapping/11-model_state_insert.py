#!/usr/bin/python3
"""A script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import sessionmaker
from sqlalchemy.orm import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    add_st = State(name='Louisiana')
    session.add(add_st)
    session.commit()
    print(add_st.id)
    session.close()
