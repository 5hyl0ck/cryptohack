#! /usr/bin/env python

mod =  29
numbers = [14,6,11] 
roots = []

for j in numbers:
	for i in range(mod - 1):
		rez = (i ** 2) % mod

		if rez == j:
			roots.append(i)		
		


print(f"the smallest quadratic residue is {min(roots)}")