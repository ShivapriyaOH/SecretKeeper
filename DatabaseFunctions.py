#!/usr/bin/python

import MySQLdb
def create_database():
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
  return 

def insert_database(key,value):
  # Open database connection
  db = MySQLdb.connect("localhost","root","hahaha","main")
   
  # prepare a cursor object using cursor() method
  cursor = db.cursor()
 # Insert into table
 # key=raw_input("Enter a key that you want to save")
 # print(key)
 # value=raw_input("Enter a value for the key")
  sql = "INSERT INTO SECRETS VALUES('%s','%s')" % (key,value)
  
  try:
     # Execute the SQL command
     cursor.execute(sql)
     # Commit your changes in the database
     db.commit()
  except:
     # Rollback in case there is any error
     db.rollback()
  
  print("Saved !")
  # disconnect from server
  db.close()
  return

def retrieve_database(key):
  # Open database connection
  db = MySQLdb.connect("localhost","root","hahaha","main")
  
  # prepare a cursor object using cursor() method
  cursor = db.cursor(MySQLdb.cursors.DictCursor)
  sql = "SELECT SECRET_VALUE FROM SECRETS WHERE SECRET_KEY='%s'" % (key) 
  try:
     # Execute the SQL command
     cursor.execute(sql)
     result_set=cursor.fetchone()
     # Commit your changes in the database
     db.commit()
  except:
     # Rollback in case there is any error
     db.rollback()
  
  # disconnect from server
  db.close()
  return result_set
