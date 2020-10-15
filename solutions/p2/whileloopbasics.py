# 0. Create a program that prints out the numbers from 1 to a user entered number, then back down to 1

'''
num = int(input('Enter a number: '))

start = 1

while start <= num:
    print(start)
    start += 1

while start > 1:
    start -= 1
    print(start)
'''

# 1. Create a program that makes the user continuously guess a WORD (string) until they get the secret word right. 

secret = 'McDonalds'
user_input = '' # EMPTY STRING
counter = 0

while user_input != secret and counter < 5:
    user_input = input('Enter the secret word: ')
    if user_input != secret:
        counter += 1
# end of while loop

if counter == 5:
    print('You have guessed too many times.')
else:
    print(secret)
