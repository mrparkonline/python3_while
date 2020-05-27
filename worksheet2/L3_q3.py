# Invalid String
# Park
# 03.13.2020
# This is an awful solution, we will learn how to do this a lot better
# later in the course

# IPO
invalid = True
user_input = ''

while invalid:
    user_input = input('Enter a value: ')

    if '!' in user_input:
        invalid = True
    elif '@' in user_input:
        invalid = True
    elif '$' in user_input:
        invalid = True
    elif '%' in user_input:
        invalid = True
    elif '^' in user_input:
        invalid = True
    elif '&' in user_input:
        invalid = True
    elif '*' in user_input:
        invalid = True
    elif '0' in user_input:
        invalid = True
    elif '1' in user_input:
        invalid = True
    elif '2' in user_input:
        invalid = True
    elif '3' in user_input:
        invalid = True
    elif '4' in user_input:
        invalid = True
    elif '5' in user_input:
        invalid = True
    elif '6' in user_input:
        invalid = True
    elif '7' in user_input:
        invalid = True
    elif '8' in user_input:
        invalid = True
    elif '9' in user_input:
        invalid = True
    else:
        invalid = False

print('Valid input:,' user_input)
