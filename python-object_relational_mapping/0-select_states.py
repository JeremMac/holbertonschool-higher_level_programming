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
        exit(1)

    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")

for i in cursor.fetchall():
    print(i)

cursor.close()
conn.close()
