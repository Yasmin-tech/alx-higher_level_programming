#!/usr/bin/python3
""" This moudel contain a script that lists all cities from the database
hbtn_0e_4_usa """

import MySQLdb
import sys


def get_cities():

    """lists all cities in the givin database """
    uname = sys.argv[1]
    upass = sys.argv[2]
    dbname = sys.argv[3]

    # database object connection
    db = MySQLdb.connect(host="localhost", user=uname,
                         password=upass, database=dbname, port=3306)

    # create a cursor to the database
    cur = db.cursor()

    # execute the query

    query = "SELECT * FROM {}.cities ORDER BY id ASC".format(dbname)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    get_cities()
