# 6. Square and Cubes of Numbers
 
#Create a program that outputs the square of N and the cube of N of all numbers from 2 to N, where N is the user input, type integer, greater than 2.

num = int(input('Enter the upper limit: '))

starting_num = 2

while starting_num <= num:
    print(starting_num, starting_num ** 2, starting_num ** 3)

    starting_num += 1
# end of while loop