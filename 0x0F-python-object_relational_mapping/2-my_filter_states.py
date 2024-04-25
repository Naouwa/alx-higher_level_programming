#!/usr/bin/python3
"""It takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Configuring the database"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
    )

    """Creating the connection"""
    connect = db.cursor()
    connect.execute("SELECT * FROM `states` WHERE \
            BINARY `name` = '{}'".format(sys.argv[4]))
    states = connect.fetchall()
    [print(state) for state in states]
