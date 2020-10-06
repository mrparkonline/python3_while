
# Create a program that asks for 10 floating point numbers; calculate the total sum, total product, and average of the 10 numbers.

total_sum = 0
total_product = 1

counter = 0
while counter < 10:
    current_float_num = float(input('Enter a floating point: '))
    total_sum += current_float_num
    total_product *= current_float_num

    counter += 1
# end of while

average = total_sum / 10

print('The total sum of the 10 inputs is:', total_sum)
print('The total product of the 10 inputs is:', total_product)
print('The average of the 10 inputs is:', average)
