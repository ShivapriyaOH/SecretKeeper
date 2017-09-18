#!/usr/bin/python
secretDictionary ={}
print("Welcome to your Secret Keeper")
print("Don't you worry, your secrets are safe here :)")
while(True):
  key=raw_input("Enter a key that you want to save")
  print(key)
  value=raw_input("Enter a value for the key")
  secretDictionary[key]=value
  print("Saved !")
  print("Do you have more secrets to save(y/n) ?")
  x = raw_input()
  if x == 'y':
     True
  else :
     False
     print("Bye!")
     break
print(secretDictionary)

