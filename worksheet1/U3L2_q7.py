# Mr. Park
# Solutions
# 10.15.18
# Multiples of 3 or 5

# variable initialization
start = 1
total_sum = 0

# input
num = int(input("Enter a value greater than 5: "))

# processing & output
while start <= num:
	if start % 3 == 0 or start % 5 == 0:
		total_sum += start

	start += 1
# end of while

print('The total sum of all numbers under:', num, 'that are divisible by 3 or 5 is:', total_sum)
