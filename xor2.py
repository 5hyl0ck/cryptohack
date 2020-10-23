#!/usr/bin/env python3 
from pwn import xor

key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
secxor = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
trdxor = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
fthxor = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
#due to the commutative and self inverse laws, an xored string can be xored with one of the operands to
#reveal the other
key2 = xor(key1,secxor)
key3 = xor(trdxor,key2)
# running this on an already xored string
buffer = xor(key1,trdxor)
flag = xor(fthxor,buffer) 
print(flag)

