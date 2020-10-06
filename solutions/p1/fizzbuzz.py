# “FizzBuzz.” From 1 to 50, if the number is a multiple of three: print “Fizz”, if the number is a multiple of five: print “Buzz”, if they are multiples of both: print “FizzBuzz” otherwise print the number

num = 1 # this is our starting point

while num <= 50: # we end when num is greater than 50.

    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

    num += 1 # I increase my num by 1 at every iteration of the while loop
# end of while loop