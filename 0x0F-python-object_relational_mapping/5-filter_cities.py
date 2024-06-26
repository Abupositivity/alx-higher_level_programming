#!/usr/bin/python3

"""lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
    )

    state_name = sys.argv[4]

    cursor = db.cursor()
    query = """
        SELECT cities.name
        FROM cities
        LEFT JOIN states ON states.id = cities.state_id
        WHERE states.name = %s
    """

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    cities = ", ".join(row[0] for row in rows)
    print(cities)

    cursor.close()
    db.close()
