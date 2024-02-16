#!/usr/bin/python3
'''Module connects to MySQLdb.
connect to a MySQL server running on localhost at port 3306,
the query  lists all cities of that state passes as an argument
'''

import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""
    SELECT name FROM cities
        WHERE state_id = (
           SELECT id FROM states
               WHERE name = %s
        )
        ORDER BY id;""", (argv[4],))

    print(', '.join(r[0] for r in cur._rows))
    cur.close()
    conn.close()
