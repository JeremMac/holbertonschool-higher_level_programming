#!/usr/bin/python3
"""
Module that list all states from a database.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        exit(1)

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
    )

    cursor = database.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}'\
                    ORDER BY states.id".format(sys.argv[4]))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()
