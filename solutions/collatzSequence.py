# Collatz Sequence

# input
starting_num = int(input('Enter your starting number: '))

# processing & output
while starting_num != 1:
    print(starting_num)
    if starting_num % 2 == 0:
        starting_num //= 2
    else:
        starting_num *= 3
        starting_num += 1
# end of while loop
print(starting_num, 'and the sequence has ended.')