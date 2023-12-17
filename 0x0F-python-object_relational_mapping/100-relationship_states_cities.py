#!/usr/bin/python3
""" This module contains a script that creates the State “California”
with the City “San Francisco”
from the database hbtn_0e_100_usa
"""


from relationship_state import State, Base
from relationship_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    uname = sys.argv[1]
    upass = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(f"mysql://{uname}:{upass}@localhost:3306/{dbname}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco")

    new_state.cities.append(new_city)
    session.add(new_state)
    session.add(new_city)
    session.commit()
