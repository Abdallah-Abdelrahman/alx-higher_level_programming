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
    query = """SELECT * FROM `states`
                WHERE `states`.name LIKE "{}"
                ORDER BY `states`.id ASC;""".format(argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    conn.close()
