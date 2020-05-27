# Sharing of Factors
# Park
# 03.13.2020

# input
num1 = int(input('Enter a value: '))
num2 = int(input('Enter another value: '))

# processing & output
upper_limit = min(num1,num2)
# we set an upper_limit because we cannot share factor that is greater than
# the smaller value

factor = 1 # starting point

while factor <= upper_limit:
    if num1 % factor == 0 and num2 % factor == 0:
        print(factor, 'is shared by', num1, 'and', num2)

    factor += 1
# end of while loop
