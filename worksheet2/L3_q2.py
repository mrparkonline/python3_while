# Mr. Park
# Solutions
# 10.15.18
# Average Calculator

# Create a program that calculates the averages of the marks that user inputs. The user is allowed to input any amounts of marks they want as long it is 0 to 100.

import math

# variable initialization
counter = 0 # number of marks
total_sum = 0 # total sum of marks
average = 0 # the average is total_sum / counter
exit_loop = False

# processing
while not(exit_loop):
	mark = int(input("Enter a mark: "))
	if not(mark > 100 or mark < 0):
		total_sum += mark
		counter += 1
	# end of if

	# Loop Exit Prompt
	print('--')
	print("Would you like to exit the loop?")
	print('--')
	exit_counter = input("'Y' or 'N'")

	if exit_counter == 'Y' or exit_counter == 'y':
		exit_loop = True
	# end of loop exit Prompt
# end of while

# average calculation
average = math.ceil(total_sum / counter)
print('--')
print('The average is:', average)
