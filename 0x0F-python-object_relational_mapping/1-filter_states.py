#!/usr/bin/python3
"""lists all states with a name starting with
N (upper N) from the database
"""
import MySQLdb
import sys

if __name__ == "__main__":
     db = MySQLdb.connect(user=sys.argv[1],
             passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM `states` ORDER BY `id`")
    (print (state) for state in curs.fetchall() if state[1][0] == "N")
