#!/usr/bin/python3
""" It takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == '__main__':
    """Configuring the database"""
    db = MySQLdb.connect(host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset='utf8'
    )

    """Creating the connection"""
    connect = db.cursor()
    connect.execute("SELECT cities.name FROM cities JOIN states \
            ON cities.state_id = states.id WHERE states.name LIKE %s \
            ORDER BY cities.id", (sys.argv[4],))
    cities = connect.fetchall()
    print(", ".join(city[0] for city in cities))
    connect.close()
    db.close()
