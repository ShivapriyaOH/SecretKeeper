#!/usr/bin/python
from Crypto.Cipher import XOR
import base64

def encrypt(passkey, plaintext):
  cipher = XOR.new(passkey)
  return base64.b64encode(cipher.encrypt(plaintext))

def decrypt(passkey, ciphertext):
  cipher = XOR.new(passkey)
  return cipher.decrypt(base64.b64decode(ciphertext))
