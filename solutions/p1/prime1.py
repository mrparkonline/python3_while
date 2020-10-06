# 9a) Prime Checker
# Is this number prime???

# input
num = int(input('Enter a number to check if number is prime: '))

# processing & output
divisor = 1
factor_counter = 0

while divisor <= num:
    if num % divisor == 0:
        print(divisor, 'is a factor')
        factor_counter += 1
    
    # end of if
    divisor += 1
# end of while

print('There are', factor_counter, 'factors.')

if factor_counter != 2:
    print(num, 'is a composite number.')
else:
    print(num, 'is a prime number.')