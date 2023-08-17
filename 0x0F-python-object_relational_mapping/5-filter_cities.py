#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor
    cursor = db.cursor()

    # Execute SQL query to get city names of the specified state
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all results
    results = cursor.fetchall()

    # Close cursor and database connection
    cursor.close()
    db.close()

    # Display results
    city_names = [result[0] for result in results]
    print(", ".join(city_names))
