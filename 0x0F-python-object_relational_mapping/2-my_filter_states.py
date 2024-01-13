#!/usr/bin/python3
""" It takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument."""

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
    connect.execute(
            "SELECT * FROM states WHERE CONVERT(`name USING Latin1`)\
                    COLLATE Latin1_General_CS = '{}';".format(sys.argv[4]))
    states = connect.fetchall()

    for state in states:
        print(state)
