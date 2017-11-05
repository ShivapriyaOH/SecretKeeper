#!/usr/bin/python
import CrypticFunctions
import DatabaseFunctions
import getpass

class SecretKeeper:
   'A private vault to safe keep the information in key:value pairs'

   def __init__(self):
     print("Welcome to your Secret Keeper")
     print("Don't you worry, your secrets are safe here :)")

   def createDB(self):
     DatabaseFunctions.create_database()

   def validateKey(self,key):
     if(key == ""):
       print("ERROR: Null key is not permitted")
       return False
     #elif():
      # print("ERROR: Keys must be unique in the Secret Keeper")
       #return False
     else:
       return True
 
   def setAttr(self,key,passkey,value):
     ciphervalue = CrypticFunctions.encrypt(passkey,value)
     DatabaseFunctions.insert_database(key,ciphervalue)
  
   def getAttr(self,key,passkey):
     dict_value = DatabaseFunctions.retrieve_database(key)
     if dict_value==():
        print("There are no keys matching. Try again. ")
        return
     print ("KEY:VALUES matching your search")
     for row in dict_value:
       print row[0],":",CrypticFunctions.decrypt(passkey,row[1])

obj = SecretKeeper()
passkey = getpass.getpass("Enter the password to encrypt/decrypt your vault (no space allowed): ")
while(True):
   print("***************************************************************\n Here is what you can do in the Secret Keeper: ")
   print(" 1: Create a new secrets database \n 2: Save a secret in the form key:value  \n 3: Retrieve a secret given a key \n 4: Exit \n")
   print("***************************************************************\n")
   option = raw_input()
   if(option =='1'):
     obj.createDB()
     print("New Database is created")
   elif(option == '2'):
     inputkey=raw_input("Enter a key that you want to save: ")
     while(obj.validateKey(inputkey) != True):
       inputkey=raw_input("Enter a valid key: ").trim()
     value=raw_input("Enter a value for the key: ")
     obj.setAttr(inputkey,passkey,value)
     print("New information has been saved in the vault ! \n *******************************************")
   elif(option == '3'):
     print("Enter the key for which you want to retrieve information: ")
     retrievekey = raw_input() 
     print("*************************************************************\n")
     obj.getAttr(retrievekey,passkey)
     print("*************************************************************\n")
   elif(option == '4'):
     print("Thank you for using Secret Keeper. Bye, See you soon! :) \n ****************************************************")
     break
   else:
     print("Invalid input. Try again")

