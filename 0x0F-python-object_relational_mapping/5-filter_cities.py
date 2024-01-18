#!/usr/bin/python3
""" It takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == '__main__':
    """Configuring the database"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset='utf8')

    """Creating the connection"""
    con = db.cursor()
    con.execute("SELECT * FROM `cities` as `con` \
                 INNER JOIN `states` as `st` \
                 ON `con`.`state_id` = `st`.`id` \
                 ORDER BY `con`.`id`")
    cities = connect.fetchall()
    print(", ".join([city[2] for city in cities if city[4] == sys.argv[4]]))
    connect.close()
    db.close()
