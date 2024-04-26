#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}'.format(
                sys.argv[1], sys.argv[2],
                sys.argv[3]), pool_pre_ping=True
                            )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    st = session.query(State).order_by(State.id).first()

    if st:
        print("{}. {}".format(st.id, st.name))
    else:
        print("Nothing")
    session.close()
