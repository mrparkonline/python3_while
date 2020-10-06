# Create a program that determines the numbers that are divisible by 7 and is a multiple of 5 between 1500 and 2700 inclusively.

start_num = 1500

while start_num <= 2700:
    if start_num % 5 == 0 or start_num % 7 == 0:
        print(start_num)
    
    start_num += 1
# end of while