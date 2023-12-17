#!/usr/bin/python3
""" This module contains a script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa"""


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

    results = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id)
    for row in results:
        print(f"{row.id}: {row.name}")
