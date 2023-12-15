#!/usr/bin/python3
# This moudel contain a script that lists all states from
# the database hbtn_0e_0_usa

import MySQLdb
import sys

def get_states():
    """lists all states in the givin database """
    uname = sys.argv[1]
    upass = sys.argv[2]
    dbname = sys.argv[3]

    # database object connection
    db = MySQLdb.connect(host="localhost",
                         user=uname, passwd=upass, db=dbname, port=3306)

    # create a cursor to the database
    cur = db.cursor()

    # execute the query

    query = "SELECT * FROM {}.states ORDER BY id ASC".format(dbname)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    get_states();
