#!/usr/bin/python3
""" This module contains a script that list all cities
in the input state"""

import sys
import MySQLdb


def get_cities_filter():
    """ Filter the the citties in the givin state"""
    uname = sys.argv[1]
    upass = sys.argv[2]
    dbname = sys.argv[3]
    sname = sys.argv[4]

    # connect to the datbase
    db = MySQLdb.connect(
        host="localhost", user=uname, password=upass,
        database=dbname, port=3306)

    # get the corsor object
    cr = db.cursor()

    query = "SELECT c.name\
             FROM cities c\
             JOIN states s\
             ON c.state_id = s.id\
             WHERE s.name = %s\
             ORDER BY c.id"
    cr.execute(query, (sname,))
    results = cr.fetchall()

    printed = False
    for result in results:
        for city in result:
            if (printed):
                print(", " + city, end="")
            else:
                print(city, end="")
                printed = True

    print()


if __name__ == "__main__":
    get_cities_filter()
