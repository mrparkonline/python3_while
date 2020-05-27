# Mr. Park
# 10.19.18
# listing all primes under N

num = int(input('Enter a value: '))
divider = 1
factor_count = 0

counter = 1

while counter < num :
	current_num = counter
	factor_count = 0 # reset at every iteration
	divider = 1 # reset at every iteration as well

	# Prime checker for counter starts here
	# WE ARE GOING TO CHECK IF CURRENT_NUM IS PRIME!
	while divider <= current_num:
		if current_num % divider == 0:
			factor_count +=1 # Counting the number of factors
		divider += 1
	if current_num == 1:
		print(current_num, "is a Composite Number")
	else:
		if factor_count <= 2:
			print(current_num, "is a Prime Number")
		else:
			print(current_num, "is a Composite Number")
	# Ends here

	counter += 1
