#!/usr/bin/python3
'''Module connects to MySQLdb.
connect to a MySQL server running on localhost at port 3306,
the query searches for certain name
'''

import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name = %s
                ORDER BY id ASC""", (argv[4],))
    row = cur.fetchone()
    print(row)
    cur.close()
    conn.close()
