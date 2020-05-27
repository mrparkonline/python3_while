# If a number has 2 factors, it is a prime!
num = int(input('Enter a value: '))
divider = 1
factor_count = 0
while divider <= num:
	if num % divider == 0:
		factor_count +=1 # Counting the number of factors
	divider += 1
if num == 1:
	print("Composite Number")
else:
	if factor_count <= 2:
		print("Prime Number")
	else:
		print("Composite Number")
