# Greatest Commmon Divisor
# Park
# U3 While Loop Review Solution

# input
num1 = int(input())
num2 = int(input())

# processing & output
gcd = 0
divider = 1
upper_limit = min(num1,num2)

while divider <= upper_limit:
    if num1 % divider == 0 and num2 % divider == 0:
        gcd = divider
    # end of if

    divider += 1
# end of while

print(gcd)
