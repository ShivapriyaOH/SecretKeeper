#!/usr/bin/python
import CrypticFunctions

class SecretKeeper:
   'A private vault to safe keep the information in key:value pairs'

   secretDictionary = dict()
   def __init__(self):
     print("Welcome to your Secret Keeper")
     print("Don't you worry, your secrets are safe here :)")

   def validateKey(self,key):
     if(key == ""):
       print("ERROR: Null key is not permitted")
       return False
     elif(key in SecretKeeper.secretDictionary):
       print("ERROR: Keys must be unique in the Secret Keeper")
       return False
     else:
       return True
 
   def setAttr(self,key,passkey,value):
     ciphertext = CrypticFunctions.encrypt(passkey,value)
     SecretKeeper.secretDictionary[key] = ciphertext
  
   def getAttr(self,key,passkey):
     value = SecretKeeper.secretDictionary.get(key)
     return CrypticFunctions.decrypt(passkey,value)
   
   def display(self):
     print(SecretKeeper.secretDictionary)


vault = SecretKeeper()
passkey = raw_input("Enter a passkey to encrypt your vault (no space allowed): ")
while(True):
   print("Here is what you can do in the Secret Keeper: ")
   print(" Enter 1 to save a secret in the form key:value \n Enter 2 to retrieve a secret given a key \n Enter 3 to exit \n")
   option = raw_input()
   if(option == '1'):
     inputkey=raw_input("Enter a key that you want to save: ")
     while(vault.validateKey(inputkey) != True):
       inputkey=raw_input("Enter a valid key: ")
     value=raw_input("Enter a value for the key: ")
     vault.setAttr(inputkey,passkey,value)
     print("New information has been saved in the vault !")
     vault.display()
   elif(option == '2'):
     print("Enter the key for which you want to retrieve information: ")
     retrievekey = raw_input()
     print("Your value is- ") 
     print(vault.getAttr(retrievekey,passkey))
   elif(option == '3'):
     print("Thank you for using Secret Keeper. Bye, See you soon! :)")
     break
   else:
     print("Invalid input. Try again")

