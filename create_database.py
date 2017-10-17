#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","hahaha","main")

# prepare a cursor object using cursor() method
cursor = db.cursor()
# Create table as per requirement
sql = """CREATE TABLE SECRETS (
         SECRET_KEY  VARCHAR(100) NOT NULL,
         SECRET_VALUE VARCHAR(200),
         PRIMARY KEY(SECRET_KEY))"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
