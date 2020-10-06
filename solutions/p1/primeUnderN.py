# 9b. Prime Numbers under N

# Create a program that lists all prime numbers under N, an integer input that is greater than 2.

upper_limit = int(input('Enter a value for N: '))

start = 2

while start < upper_limit:
    #print('My Current Number:', start)

    # CHECK TO SEE IF START IS PRIME!
    # input
    # replace our input with our current number, called start
    num = start #int(input('Enter a number to check if it is prime: '))

    # processing & output
    isPrime = True # We are going to try to debunk that num is not prime, if we cant, we will decide that num is prime.

    divisor = 2 # divisor starts at 2 because 1 is a factor for all numbers

    while divisor < num and isPrime: # isPrime == True
        # we don't check num as a divisor because num is a factor of itself
        if num % divisor == 0:
            isPrime = False
        
        divisor += 1 # make sure to increase your divisor by 1 to check all number
    # end of while loop

    if isPrime:
        print(num, 'is a prime number.')
    #else:
    #    print(num, 'is a composite number.')
    # END OF THAT CHECK
    start += 1
# end of while loop