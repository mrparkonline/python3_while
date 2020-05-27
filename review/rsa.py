# CCC J2 - 2005 RSA Numbers
# Park
# U3 While Loop Review Solution

# IPO
lower = int(input())
upper = int(input())

lower_copy = lower
rsa_counter = 0

while lower <= upper:
    factor_counter = 0
    divider = 1

    # factor counter
    while divider <= lower:
        if lower % divider == 0:
            factor_counter += 1

        divider += 1
    # end of inner while loop

    if factor_counter == 4:
        rsa_counter += 1

    lower += 1
# end of while

print('The number of RSA numbers between', lower_copy, 'and', upper, 'is', rsa_counter)
