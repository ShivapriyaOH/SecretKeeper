#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","hahaha","main")

# prepare a cursor object using cursor() method
cursor = db.cursor(MySQLdb.cursors.DictCursor)
key=raw_input("Enter a key that you want to search")
print(key)
sql1= "SELECT SECRET_VALUE FROM SECRETS WHERE SECRET_KEY='%s'" % (key)

try:
   # Execute the SQL command
   value = cursor.execute(sql1)
   result = cursor.fetchone()
#   print(value)
#   print("printing all the values"
   print(result)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
