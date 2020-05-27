# CCC J2 - 2004 CS City
# Park
# U3 While Loop Review Solution

# Since mayor is every 4 years
# treasurer is every 2 years
# programmer is every 3 years
# dog-catcher is every 5 years
# The LCM of such 4 numbers is the interval when
# all positions are refreshed

# IPO
start = int(input())
end = int(input())

lcm = 60

while start <= end:
    print('All positions change in year', start)

    start += lcm
