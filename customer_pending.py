#!/usr/bin/python

#import the mysqldb connector with mdb
import MySQLdb as mdb
import sys

#Get connected with db
con = mdb.connect('localhost', 'root', 'redhat', 'keen_ticket');

#with con: 

cur = con.cursor()
#cur.execute("SELECT * FROM keen_religare where status=0")
#cur.execute("SELECT * FROM keen_religare")
cur.execute("show tables")


rows = cur.fetchall()


for row in rows:
	for col in row:
		sys.stdout = open(col + ".csv", "w")
		print "id,Points_Man,Engineer_Name,Customer_Name,Project_Name,Case_Type,Call_Pending,Customer_Side,Keen_Side,Problem_Start_Date,Estimated_end_Date,Task_Description,Status,Call_Close_Date,Remarks,Points"
		select = cur.execute("SELECT * FROM " + col + " where status=0")
		data = cur.fetchall()
		for tmp in data:
			print tmp
			pending_calls = len(data)
		SUBJECT = "Pending calls " + str(pending_calls) + " at " + col
		select = cur.execute("SELECT DISTINCT Points_Man,Engineer_Name FROM " + col + " where status=0")
		data1 = cur.fetchall()
		for tm1 in data1:
			test = ('vikas.parashar@fosteringlinux.com','varad.gupta@fosteringlinux.com')
			TO=tm1 + (test)
		sys.stdout.close()
		attachment = col + ".csv"
		execfile("customer_mail.py")







