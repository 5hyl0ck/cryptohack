#!/usr/bin/env python3 

from pwn import xor

ciphertext = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
plain = "crypto{"
newkey = ''
	
for i in range(len(plain)):
	newkey += chr(ord(plain[i]) ^ ciphertext[i]) 

newkey += 'y'
newkey = newkey.encode('utf-8') 

flag = xor(newkey,ciphertext)
print(newkey)
print(flag)




