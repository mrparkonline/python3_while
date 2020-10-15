m_die = int(input('Enter the number of sides for die 1: '))
n_die = int(input('Enter the number of sides for die 2: '))

# processing & output
number_m = 1 # m_die results
number_n = 1 # n_die results
ten_counter = 0

while number_m <= m_die:
    
    number_n = 1 # We have to always reset number_n back to 1 

    while number_n <= n_die:
        current_roll = number_m + number_n

        if current_roll == 10:
            ten_counter += 1
        
        number_n += 1
    # end of inner while loop
    number_m += 1
# end of outer while loop
print('There are', ten_counter, 'ways.')