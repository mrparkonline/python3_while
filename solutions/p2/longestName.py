# Longest Name.

# Create a program that takes an unknown amount of names and outputs the longest name. You will know that the inputs are done when the user has inputted a string of X

user_input = '' # Empty string

longest_name = ''
length = 0

while user_input != 'X':

    user_input = input('Enter a name: ')

    if user_input != 'X':
        current_length = len(user_input) # determining how long the name is

        if current_length > length:
            length = current_length
            longest_name = user_input
# end of while

print(longest_name, 'was the longest name with', length, 'characters.')