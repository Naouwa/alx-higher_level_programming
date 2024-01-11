#!/usr/bin/python3
"""A script that lists all states from database htbn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    """Configuring the database"""
    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], charset="utf8"
    )

    """Creating the connection"""
    connect = MySQLdb.connect(**db)
    cursor = connect.cursor()

    """Executing the command to get all states by asc order"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """Fetching all the rows"""
    rows = cursor.fetchall()

    """Showing the results"""
    for row in rows:
        print(row)

    """Closing the connection and the cursor"""
    cursor.close()
    connect.close()
