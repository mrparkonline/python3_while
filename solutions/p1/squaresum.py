# Sum of Squares

# processing & output

start = 2
total_sum = 0

while total_sum <= 200:
    total_sum += start ** 2

    start += 1
    print('Currently total_sum is:', total_sum)