# 7. Multiples of 3 or 5
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Create a program that finds the sum of all the multiples of 3 or 5 below 1000
Improve the program so that it finds the sum of all the multiples of 3 or 5 below N where N is greater than 3.
'''

upper_limit = int(input('Enter the upper_limit: '))
start = 3

total_sum = 0 # this variable will keep track of total sum

while start < upper_limit:
    if start % 3 == 0 or start % 5 == 0:
        total_sum += start

    start += 1

print('The total sum of all values under', upper_limit, 'that are multiples of 3 or 5 is:', total_sum)