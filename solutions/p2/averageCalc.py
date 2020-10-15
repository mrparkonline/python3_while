# Average Calculator

# Create a program that calculates the averages of the marks that user inputs. The user is allowed to input any amount of marks they want as long as it is 0 to 100.

mark_counter = 0 # this variable counts how many marks I have
total_sum = 0 # this variable tracks the total sum of my marks

flag = True # as long as flag is True, we loop

while flag:
    current_mark = int(input('Enter a mark from 0 to 100: '))

    if current_mark < 0 or current_mark > 100:
        print('Invalid Mark.')
    else:
        total_sum += current_mark
        mark_counter += 1
    
    # check to see if the user wants to add another mark
    user_input = input('Do you want to add another mark? (Y/N): ')

    if user_input == 'N':
        flag = False
# end of while

average = total_sum / mark_counter
print('Your average is:', average)