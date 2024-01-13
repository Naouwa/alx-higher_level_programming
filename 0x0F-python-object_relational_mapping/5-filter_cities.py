#!/usr/bin/python3
""" It takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""

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
    state_name = sys.argv[4]
    connect.execute("SELECT * FROM `cities` as `connect` \
            INNER JOIN `states` as `st` \
            ON `connect`.`state_id` = `st`.`id` \
            ORDER BY `connect`.`id`")
    cities = connect.fetchall()

    print(", ".join([city[2] for city in cities if city[4] == argv[4]]))
