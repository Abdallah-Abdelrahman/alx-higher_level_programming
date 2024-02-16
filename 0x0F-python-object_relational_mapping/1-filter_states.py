#!/usr/bin/python3
'''Module connects to MySQLdb.
connect to a MySQL server running on localhost at port 3306,
the query filters results start with `N`
'''

import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
                WHERE BINARY name LIKE 'N%'
                ORDER BY id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print((row))
    cur.close()
    conn.close()
