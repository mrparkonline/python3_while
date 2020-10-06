
# Group Placement Solution

# input
win_counter = 0 # we are going to increase the counter, per win

number_of_games = 0 # we are going to increase this until 6

while number_of_games < 6:
    game_result = input('Enter the result of your game (W/L): ')

    if game_result == 'W':
        win_counter += 1
    
    number_of_games += 1
# end of while

print('Currently, win_counter is:', win_counter)
print('Currently, number_of_games is:', number_of_games)

if win_counter >= 5:
    print('You are in group', 1)
elif win_counter >= 3:
    print(2)
elif win_countner >= 1:
    print(3)
else:
    print(-1)