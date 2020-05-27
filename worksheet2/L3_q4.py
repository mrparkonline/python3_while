# Longest Name
# Park
# 03.13.2020
# Purpose: What to do when you don't know when the loop ends

# Initialization
user_input = '' # blank string to hold user input of names
# when user_input is 'X' we will terminate the loop

longest_length = 0 # initial comparison length value
result_name = '' # name holding variable that will contain the longest length

while user_input != 'X': # we loop when user_input is not 'X'
    user_input = input('Enter a name: ')

    if user_input != 'X':
        if len(user_input) > longest_length:
            # the new inputted name is longer than the previous
            # longest length

            longest_name = len(user_input) # update with new value
            result_name = user_input
    # end of if
# end of while

print('The longest name:', result_name)
