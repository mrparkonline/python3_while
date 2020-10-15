# RPS Game~ w/ LOOP

from random import choice # this helps us create the CPU

flag = True

while flag:
    
    print('RPS GAME')
    print('--------')
    print('Welcome to Rock Paper Scissors!')
    player_choice = input('Choose your option (R, P, S): ')

    cpu_choice = choice('RPS') # cpu is going to choose a single character from R,P,S

    if player_choice == cpu_choice:
        print('TIE GAME.')
    else:
        if player_choice == 'R':
            if cpu_choice == 'P':
                print('CPU WINS')
            else:
                print('YOU WIN!')
        
        elif player_choice == 'P':
            if cpu_choice == 'R':
                print('YOU WIN!')
            else:
                print('CPU WINS')
        
        else:
            # player chose Scissors
            if cpu_choice == 'R':
                print('CPU WINS')
            else:
                print('YOU WIN!')
    # end of conditionals for checking who won the game

    # Check to see if the humans want to lose again ...
    # (AKA: check to see if the player wants to play again)
    user_input = input('Do you want to play again? (Y/N): ')

    if user_input == 'N':
        flag = False
        print('Thank you for playing RPS.')
# end of while loop