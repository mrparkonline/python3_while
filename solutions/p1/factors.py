# Factors a number

# input
num = int(input('Enter a number: '))

# processing & output

divider = 1 # this is our conditional variable
# our while loop depends on the value of this variable

while divider <= num:

    # Check if divider is a factor of num
    if num % divider == 0:
        # divider is a factor!
        print(divider, 'is a factor of:', num)
    
    divider += 1
# end of while

print('The program has finished.')