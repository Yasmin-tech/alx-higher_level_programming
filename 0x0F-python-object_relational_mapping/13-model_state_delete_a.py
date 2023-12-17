#!/usr/bin/python3
""" This module contains a script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa"""


from model_state import State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    uname = sys.argv[1]
    upass = sys.argv[2]
    dbname = sys.argv[3]

    # connect to the engine and create a session
    engine = create_engine(f"mysql://{uname}:{upass}@localhost:3306/{dbname}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # get reference to the objects to delete
    objs_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    if objs_to_delete:
        for obj in objs_to_delete:
            session.delete(obj)
        session.commit()
