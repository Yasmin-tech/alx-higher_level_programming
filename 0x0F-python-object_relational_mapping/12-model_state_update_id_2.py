#!/usr/bin/python3
""" This module contains a script that changes the name of a
State object(id = 2 to New Mexico)
from the database hbtn_0e_6_usa"""


from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    uname = sys.argv[1]
    upass = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(f"mysql://{uname}:{upass}@localhost:3306/{dbname}")
    Session = sessionmaker(bind=engine)
    session = Session()

    state_obj = session.query(State).filter(State.id == 2).first()
    state_obj.name = "New Mexico"

    session.add(state_obj)
    session.commit()

    # update_state = session.query(State).filter(State.id == 2).first()
    # print(f"{update_state.id}: {update_state.name}")
