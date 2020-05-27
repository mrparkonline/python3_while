# Mr. Park
# Solutions
# 10.15.18
# Create a program that determines the numbers that are divisible by 7 and is a multiple of 5 between 1500 and 2700 inclusively.

# variable
start = 1500

print("Numbers from 1500 to 2700 that are divisible 5 or 7.")
while start <= 2700:
	if (start % 5) == 0 or (start % 7) == 0:
		print(start)

	start += 1
# end of if
