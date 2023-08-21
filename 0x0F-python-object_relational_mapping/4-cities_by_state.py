#!/usr/bin/python3
"""lists all cities from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = db.cursor()
    curs.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    records = curs.fetchall()
    for record in records:
        print(record)
    curs.close()
    db.close()
