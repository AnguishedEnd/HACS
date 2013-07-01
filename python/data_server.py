#!/usr/bin/python

import MySQLdb
import serial
import time
from mysqldb_connection import dsn

# Open database connection
db = MySQLdb.connect( host=dsn['host'], 
		      user=dsn['user'],
		      passwd=dsn['passwd'],
		      db=dsn['db'])

ser = serial.Serial('COM3', 9600)

while(1):

   # prepare a cursor object using cursor() method
   cursor = db.cursor()

   # Prepare SQL query to INSERT a record into the database.
   sql = "SELECT * FROM arduino"

   try:
      # Execute the SQL command
      cursor.execute(sql)
      # Fetch all the rows in a list of lists.
      results = cursor.fetchall()
      for row in results:
         d0 = row[0]
         # Now print fetched result
         #print "LightState is %s" % (lightstate)

   except:
      print "Error: unable to fetch data"


   time.sleep(1)
   ser.write(d0)
