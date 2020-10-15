# RSA NUMBERS
# numbers that have 4 factors

# input
start = int(input('Enter a starting value: '))
end = int(input('Enter the ending value: '))

# processing & output
num = start # we will use num to see which numbers are RSA numbers
rsa_counter = 0 # everytime we find a RSA number, increase the counter

while num <= end:
    
    # Inner while loop problem
    # How many factors does num have?
    factor_counter = 0
    divisor = 1

    while divisor <= num:
        if num % divisor == 0:
            factor_counter += 1
        
        divisor += 1
    # end of inner problem

    if factor_counter == 4:
        # WE HAVE AN RSA NUMBER!!!
        rsa_counter += 1

    num += 1 # increasing num until it is greater than end
# end of while loop.

print('There are', rsa_counter, 'RSA numbers from', start, 'to', end)