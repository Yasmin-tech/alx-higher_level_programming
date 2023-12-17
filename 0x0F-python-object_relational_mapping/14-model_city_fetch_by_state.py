#!/usr/bin/python3
""" This module contains the code that prints all City objects
from the database hbtn_0e_14_usa"""


from model_state import Base, State
from model_city import City
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

    for c, s in session.query(City, State).\
            filter(City.state_id == State.id).\
            order_by(City.id).all():
        print(f"{s.name}: ({c.id}) {c.name}")
