#!/usr/bin/python3
""" This module contains  a script that prints the first State
object from the database hbtn_0e_6_usa"""


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

    result = session.query(State).first()

    if result:
        print(str(result.id) + ": " + result.name)
    else:
        print("Nothing")
