#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","hahaha","main")

# prepare a cursor object using cursor() method
cursor = db.cursor()
# Insert into table
key=raw_input("Enter a key that you want to save")
print(key)
value=raw_input("Enter a value for the key")
sql2 = "INSERT INTO SECRETS VALUES('%s','%s')" % (key,value)

try:
   # Execute the SQL command
   cursor.execute(sql2)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

print("Saved !")
# disconnect from server
db.close()
