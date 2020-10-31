
def calculate(number1, number2):
	x = number1
	y = number2

	while y != 0:
		r = x % y
		x = y
		y = r

	return x


# basic function to calculate the GCD using the euclidean algorithm


number1 = input("please enter the first number: ")

number2 = input("please enter the second number: ")


print("the GCD is " + str(calculate(number1,number2)))