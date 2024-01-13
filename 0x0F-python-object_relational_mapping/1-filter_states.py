#!/usr/bin/python3
""" A script that  lists all states with a name starting with N
from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == '__main__':
    """Configuring the database"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset='utf8'
    )

    """Creating the connection"""
    connect = db.cursor()
    connect.execute("SELECT * FROM `states` ORDER BY `id`")
    states = connect.fetchall()
    [print(state) for state in states if state[1][0] == "N"]
