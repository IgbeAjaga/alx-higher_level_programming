#!/usr/bin/python3
"""takes in arguments and displays all values and 
matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = db.cursor()
    match = sys.argv[4]
    curs.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    records = curs.fetchall()
    for record in records:
        print(record)
    curs.close()
    db.close()
