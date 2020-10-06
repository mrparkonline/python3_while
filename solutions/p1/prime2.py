# 9a) Solution 2

# input
num = int(input('Enter a number to check if it is prime: '))

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
else:
    print(num, 'is a composite number.')