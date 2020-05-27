# Mr. Park
# Solutions
# 10.15.18
# Create a program that asks for 10 floating point numbers; calculate the sum, product, and average of them.

# variable initializations
total_sum = 0
total_product = 1 # Why would this be 1?
average = 0
counter = 0

while counter < 10:
	current_num = float(input("Enter a floating point value: "))
	total_sum += current_num
	total_product *= current_num

	counter += 1 # what is the purpose of this counter?
# end of while
average = total_sum / 10

# output
print('Total sum:', total_sum)
print('Total product:', total_product)
print('Average:', average)
