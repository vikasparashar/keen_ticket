#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'redhat', 'keen_ticket');

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM keen_religare")

    rows = cur.fetchall()

    for row in rows:
        print row
