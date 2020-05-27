# Mr. Park
# 10.19.18
# From 1 to N, where N is an integer greater one; We will output the number between 1 to N inclusively that has the most number of factors.

# Example from numbers 1 to 5. The number 4 has the most factors.

# input
upper_limit = int(input("Enter a number: "))
num = 1
max_count = 0 # This variable will hold the maximum amount of factors
max_number = 0 # This variable will hold the number with the most factor

while num <= upper_limit:
	counter = 0
	divider = 1

	while divider <= num:
		if num % divider == 0:
			counter += 1 # we found a factor; therefore, we increase counter

		divider += 1
	# WE FOUND THE NUMBER OF FACTORS

	if counter > max_count:
		max_count = counter # Replace the old max count, with the new max count
		max_number = num # Replace the old number with the new number

	num += 1 # increase our num, so that we can count the number of factors
# end of while

print(max_number, "hast the most number of factors with:", max_count, "factors.")
