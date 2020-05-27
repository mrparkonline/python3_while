# CCC J2 - 2006 Dice Game
# Park
# U3 While Loop Review Solution

# IPO
m_sides = int(input())
n_sides = int(input())

m_roll = 1 # initialization

counter = 0

while m_roll <= m_sides:
    n_roll = 1 # initialization
    while n_roll <= n_sides:
        if m_roll + n_roll == 10:
            counter += 1

        n_roll += 1
    # end of inner while
    m_roll += 1
# end of outer while

print('There are', counter, 'ways.')
