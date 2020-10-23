#!/usr/bin/env python3
<<<<<<< HEAD
=======

>>>>>>> b0da0132c01df93654359eb2c956660ce27ab367
from pwn import * 
import json
import binascii
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')
<<<<<<< HEAD
		
=======
	
	
>>>>>>> b0da0132c01df93654359eb2c956660ce27ab367
def main():		
    received = json_recv()
    to_send = {"decoded": solveChallenge(received)}
    json_send(to_send)
    print(to_send)

<<<<<<< HEAD
=======

>>>>>>> b0da0132c01df93654359eb2c956660ce27ab367
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(stuff):
    request = json.dumps(stuff).encode()
    r.sendline(request)
    
<<<<<<< HEAD
=======


>>>>>>> b0da0132c01df93654359eb2c956660ce27ab367
def solveChallenge(received):
    if received["type"] == "base64":
        decoded =  base64.b64decode(received["encoded"]).decode("utf-8")
    elif received["type"] == "hex":
        decoded = binascii.unhexlify(received["encoded"]).decode("utf-8")
    elif received["type"] == "rot13":
        decoded = codecs.decode(received["encoded"], 'rot_13')
    elif received["type"] == "bigint":
        decoded = binascii.unhexlify(received["encoded"][2:]).decode("utf-8")
    elif received["type"] == "utf-8":
        decoded = ""
        temp = received["encoded"]
        for i in temp:
            decoded = decoded + chr(i)
    return decoded
<<<<<<< HEAD
                
=======
        
        
>>>>>>> b0da0132c01df93654359eb2c956660ce27ab367
i = 0        
while i < 101:
    print("level " + str(i))
    main()
    i = i + 1