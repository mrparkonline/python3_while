# Create a program that grabs a user input from the user. The rule is that, the string input cannot contain numbers nor !@$%^&*. the input was invalid

user_input = '' # an empty string evaluates to False, in a boolean scenario

while not user_input:
    
    user_input = input('Enter an input: ')

    if '0' in user_input or '1' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '2' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '3' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '4' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '5' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '6' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '7' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '8' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '9' in user_input:
        print('Invalid input.')
        user_input = ''
    # !@$%^&*
    elif '!' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '@' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '$' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '%' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '^' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '&' in user_input:
        print('Invalid input.')
        user_input = ''
    elif '*' in user_input:
        print('Invalid input.')
        user_input = ''
    else:
        print('It was valid input!')
# end of while loop.