#!/usr/bin/python3
#!/usr/bin/python3
"""
Module that list all states from a database.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = database.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id;")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()