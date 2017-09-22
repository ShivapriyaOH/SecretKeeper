#!/usr/bin/python
secretDictionary ={}
print("Welcome to your Secret Keeper")
print("Don't you worry, your secrets are safe here :)")
fileHandle=open("my_dictionary.txt","a")
while(True):
  key=raw_input("Enter a key that you want to save")
  fileHandle.write(key)
  fileHandle.write(':')
  value=raw_input("Enter a value for the key")
  fileHandle.write(value)
  fileHandle.write('\n')
  print("Saved !")
  print("Do you have more secrets to save(y/n) ?")
  x = raw_input()
  if x == 'y':
     True
  else :
     False
     break
fileHandle.close()


