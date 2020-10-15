# When given two positive integers greater than 1 which are A and B, write a program that prints all the factors that they both share.

# 10 and 24 shares:
# 1
# 2

# input
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

# processing & output
divisor = 1
upper_limit = min(num1, num2) 

print(num1, 'and', num2, 'share these factors:')
while divisor <= upper_limit:
    if num1 % divisor == 0 and num2 % divisor == 0:
        print(divisor)
    
    divisor += 1
# end of while loop
