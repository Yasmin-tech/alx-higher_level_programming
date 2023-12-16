#!/usr/bin/python3
""" This module contains the code to fetch
all the states from states table in  hbtn_0e_6_usa database"""


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

    results = session.query(State).all()

    for row in results:
        print(str(row.id) + ": " + row.name)
