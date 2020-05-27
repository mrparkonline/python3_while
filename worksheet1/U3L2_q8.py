# Mr. Park
# Solutions
# 10.15.18
# Factor Finder

# Given an integer input greater than 0, print all its factors. 

# variable initialization & input
user_input = int(input('Enter a positive integer.'))
factor = 1

# processing & output
if user_input == 1:
	# case when user inputs 1
	print('The factor is:', 1)
else:
	while factor != (user_input + 1):
		if user_input % factor == 0:
			print('The factors are: ', factor)
		factor += 1
