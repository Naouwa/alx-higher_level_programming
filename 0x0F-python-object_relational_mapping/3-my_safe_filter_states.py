#!/usr/bin/python3
"""It takes in arguments and displays all values in
the states table of hbtn_0e_0_usa
where name matches the argument. But this time,
write one that is safe from MySQL injections!"""

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
    connect.execute("SELECT * FROM `states`")
    states = connect.fetchall()
    [print(state) for tate in states if state[1] == argv[4]]