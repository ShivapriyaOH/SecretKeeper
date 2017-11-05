#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","hahaha","main")

# prepare a cursor object using cursor() method
cursor = db.cursor(MySQLdb.cursors.DictCursor)
key=raw_input("Enter a key that you want to search")
print(key)
sql1= "SELECT * FROM SECRETS WHERE SECRET_KEY LIKE '%s'" % ("%"+key+"%")

try:
   # Execute the SQL command
   value = cursor.execute(sql1)
   result = cursor.fetchall()
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
