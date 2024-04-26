#!/sur/bin/python3
""" A script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa"""

import sys
from model_State import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    del_st = session.query(State).filter(State.name.like('%a%')).all()
    for st in del_st:
        session.delete(delete)
    session.commit()
    session.close()
