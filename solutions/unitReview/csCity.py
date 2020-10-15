# In CS City, a mathematical place to live, the mayor is elected every 4 years, the treasurer is appointed every 2 years, the chief programmer is elected every 3 years and the dog-catcher is replaced every 5 years.

# input
start_year = int(input('Enter the starting year: '))
end_year = int(input('Enter the ending year: '))

# processing & output
mayor = 4
treasurer = 2
programmer = 3
dog = 5

print('All positions change in year', start_year)

while start_year <= end_year:
    start_year += 1 # increase our year by 1

    # Each position gets closer to changing by a year
    mayor -= 1
    treasurer -= 1
    programmer -= 1
    dog -= 1

    if mayor == 0 and treasurer == 0 and programmer == 0 and dog == 0:
        print('All positions change in year', start_year)

    # resetting each position back to their normal number when they hire new
    if mayor <= 0:
        mayor = 4
    if treasurer <= 0:
        treasurer = 2
    if programmer <= 0:
        programmer = 3
    if dog <= 0:
        dog = 5

# end of while loop

''' LCM solution

while start_year <= end_year:
    start_year += 60

    if start_year <= end_year:
        print('All positions change in year', start_year)
'''