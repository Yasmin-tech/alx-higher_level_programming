#!/usr/bin/python3
""" a script that lists all City objects from the database
hbtn_0e_101_usa
using state relationship to access to the State object
linked to the City object
"""


from relationship_state import State
from relationship_city import City
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

    results = session.query(City).all()

    for city_obj in results:
        print(f"{city_obj.id}: {city_obj.name} -> {city_obj.state.name}")
