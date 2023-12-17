#!/usr/bin/python3
""" This module contains a script that lists all State objects,
and corresponding City objects, contained in the database hbtn_0e_101_usa
using the cities relationship for all State objects
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
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).all()

    for state_obj in results:
        print(f"{state_obj.id}: {state_obj.name}")
        for city_obj in state_obj.cities:
            print(f"    {city_obj.id}: {city_obj.name}")
