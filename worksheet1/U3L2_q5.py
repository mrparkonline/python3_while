# Mr. Park
# Solutions
# 10.15.18
# “FizzBuzz.” From 1 to 50, if the number is a multiple of three: print “Fizz”, if the number is a multiple of five: print “Buzz”, if they are multiples of both: print “FizzBuzz”.

# variable initialization
counter = 1

while counter <= 50:
    if counter % 3 == 0 and counter % 5 == 0:
        print('FizzBuzz')
    elif counter % 3 == 0:
		print('Fizz')
	elif counter % 5 == 0:
		print('Buzz')
	else:
		print(counter)

	counter += 1
# end of while
