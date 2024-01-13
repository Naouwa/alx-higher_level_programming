#!/usr/bin/python3
""" It lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset='utf8'
    )

    connect = db.cursor()
    connect.execute("SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states ON cities.state_id = states.id")
    states = connect.fetchall()

    for state in states:
        print(state)
