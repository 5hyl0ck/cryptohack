#!/usr/bin/env python3 

cryptostring = input('please enter the string that you want xored: ')
key = input('please enter the key: ')
result = ''

for i in cryptostring:
	result += chr(ord(i) ^ int(key))
	print('done one char')


print(result)