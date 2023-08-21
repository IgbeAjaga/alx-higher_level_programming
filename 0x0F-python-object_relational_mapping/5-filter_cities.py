#!/usr/bin/python3
"""  lists all states from the database """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = db.cursor()
    curs.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    records = curs.fetchall()
    temp = list(record[0] for record in records)
    print(*temp, sep=", ")
    curs.close()
    db.close()
