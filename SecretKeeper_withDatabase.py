#!/usr/bin/python
import CrypticFunctions
import DatabaseFunctions

class SecretKeeper:
   'A private vault to safe keep the information in key:value pairs'

   def __init__(self):
     print("Welcome to your Secret Keeper")
     print("Don't you worry, your secrets are safe here :)")

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
     value = DatabaseFunctions.retrieve_database(key)
     return CrypticFunctions.decrypt(passkey,value)
   
 #  def display(self):
     


passkey = raw_input("Enter a passkey to encrypt/decrypt your vault (no space allowed): ")
while(True):
   print("Here is what you can do in the Secret Keeper: ")
   print(" Enter 1 to save a secret in the form key:value \n Enter 2 to retrieve a secret given a key \n Enter 3 to exit \n")
   option = raw_input()
   if(option == '1'):
     inputkey=raw_input("Enter a key that you want to save: ")
     while(validateKey(inputkey) != True):
       inputkey=raw_input("Enter a valid key: ").trim()
     value=raw_input("Enter a value for the key: ").trim()
     setAttr(inputkey,passkey,value)
     print("New information has been saved in the vault !")
#     vault.display()
   elif(option == '2'):
     print("Enter the key for which you want to retrieve information: ")
     retrievekey = raw_input()
     print("Your value is- ") 
     print(getAttr(retrievekey,passkey))
   elif(option == '3'):
     print("Thank you for using Secret Keeper. Bye, See you soon! :)")
     break
   else:
     print("Invalid input. Try again")

