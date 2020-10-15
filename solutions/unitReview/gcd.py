# GCD Program

from math import gcd

# input
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

# processing & output
divisor = 1
upper_limit = min(num1, num2) 
gcd_answer = 0

#print(num1, 'and', num2, 'share these factors:')
print('GCD of', num1, 'and', num2, 'is:')
while divisor <= upper_limit:
    if num1 % divisor == 0 and num2 % divisor == 0:
        gcd_answer = divisor
    
    divisor += 1
# end of while loop
print(gcd_answer)
print('Math Module GCD:', gcd(num1,num2))