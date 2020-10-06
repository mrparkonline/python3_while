# Sum of All positive numbers under N (including N)

# input
num = int(input('Enter a value: '))

# processing & output

start = 1 # this is my conditional/repetition variable
total_sum = 0 # this contains the total sum

while start <= num:
    total_sum += start

    start += 1 # start = start + 1
# end of while