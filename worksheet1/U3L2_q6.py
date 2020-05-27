# Mr. Park
# Solutions
# 10.15.18
# Square and Cubes of Numbers

#Create a program that outputs the square of N and the cube of N of all numbers from 2 to N, where N is the user input, type integer, greater than 2.

# variable initialization
factor = 2

# input
user_input = int(input("Enter a value: "))

while factor <= user_input:
	print(factor, factor**2, factor**3)

	factor += 1
# end of while
