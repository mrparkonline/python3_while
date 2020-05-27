# Average Peanut Sizes
# Park
# 03.13.2020

# IPO
weight = 0
peanut_counter = 0
total_weight = 0

while weight != -1:
    weight = int(input('Enter the weight of a peanut: '))

    if weight != -1:
        total_weight += weight
        peanut_counter += 1
# end of while

average = total_weight / peanut_counter
print('The average weight:', average)
