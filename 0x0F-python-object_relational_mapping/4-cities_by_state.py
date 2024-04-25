#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa"""
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
    connect.execute("SELECT `connect`.`id`, `connect`.`name`, `st`.`name` \
            FROM `cities` as `connect` INNER JOIN `states` as `st` \
            ON `connect`.`state_id` = `st`.`id` ORDER BY `connect`.`id`")
    cities = connect.fetchall()
    [print(city) for city in cities]
