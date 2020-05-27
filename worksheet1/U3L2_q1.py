# Mr. Park
# Solutions
# 10.15.18
# Sum of Squares

total_sum = 0 # variable initialization
start_num = 2

while total_sum <= 200:
	print("Currently, total_sum is:", total_sum)
	total_sum += start_num**2
	start_num += 1
# end of while

print(total_sum)
