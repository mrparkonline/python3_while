# Mr. Park
# Solutions
# 10.15.18
# Guess a word; Create a program that makes the user continuously guess a WORD (string) until they get the secret word right.

secret_word = 'tacocat'

user_input = input('Guess the secret word!: ')

while user_input != secret_word:
	print('Fail!')
	user_input = input('Guess the secret word!: ')
# end of while
else:
	print('Hacking Success')
