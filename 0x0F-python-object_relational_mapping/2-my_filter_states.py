#!/usr/bin/python3
""" This moudel contain a script that and displays all
    values in the states table of hbtn_0e_0_usa
    where name matches the argument"""

import MySQLdb
import sys


def get_states_filter2():

    """lists all values in the state where its name matches the argument"""
    uname = sys.argv[1]
    upass = sys.argv[2]
    dbname = sys.argv[3]
    searching_state = sys.argv[4]

    # database object connection
    db = MySQLdb.connect(host="localhost", user=uname,
                         password=upass, database=dbname, port=3306)

    # create a cursor to the database
    cur = db.cursor()

    # execute the query

    query = "SELECT * FROM {}.\
        states WHERE BINARY name LIKE '{}' ORDER BY id ASC"\
        .format(dbname, searching_state)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    get_states_filter2()
