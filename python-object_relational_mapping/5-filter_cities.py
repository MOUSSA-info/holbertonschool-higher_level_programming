#!/usr/bin/python3
'''
This module takes in the name of a state as an argument
and lists all cities of that state
using the database hbtn_0e_4_usa
'''

import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 5:
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()

    if cities:
        print(", ".join(city[0] for city in cities))
    else:
        print("")

    cursor.close()
    db.close()
