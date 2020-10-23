from Crypto.Util.number import long_to_bytes

ciphertext = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

result = long_to_bytes(ciphertext, blocksize = 2)

<<<<<<< HEAD
print(str(result))
=======
print(str(result))
>>>>>>> b0da0132c01df93654359eb2c956660ce27ab367
