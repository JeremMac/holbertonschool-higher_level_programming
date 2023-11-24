#!/usr/bin/python3

'''
A module that contains a script that lists
all states from the database hbtn_0e_0_usa.
'''

import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("error")
        sys.exit(1)

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")

for i in cursor.fetchall():
    print(i)

cursor.close()
conn.close()
