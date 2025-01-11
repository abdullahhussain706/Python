# Rock, Scissor and Paper

import os
import random
import sys

os.system('cls')

wins = 0
losses = 0
ties = 0

while True:
    print('%s wins, %s Ties, %s losses' % (wins, losses, ties))
    while True:
        Player_input = input('Enter (r)ock (p)aper (s)cissors or (q)uit: ')
        if Player_input == 'q':
            sys.exit()
        if Player_input == 'r' or Player_input == 'p' or Player_input == 's':
            break
        else:
            print('Enter Valid Input.')

    if Player_input == 'r':
        print('Rock vs....')
    elif Player_input == 'p':
        print('Paper vs...')
    elif Player_input == 's':
        print('Scissor vs....')

    randomnum = random.randint(1, 3)

    if randomnum == 1:
        computermove = 'r'
        print('Rock')
    elif randomnum == 2:
        computermove = 'p'
        print('Paper')
    elif randomnum == 3:
        computermove = 's'

    if computermove == Player_input:
        print('It is tie!')
        ties += 1
    elif Player_input == 'r' and computermove == 's':
        print('You Win!')
        wins += 1
    elif Player_input == 'p' and computermove == 'r':
        print('You Win!')
        wins += 1
    elif Player_input == 's' and computermove == 'p':
        print('You Win!')
        wins += 1
    elif Player_input == 'r' and computermove == 'p':
        print('You lose!')
        losses += 1
    elif Player_input == 'p' and computermove == 's':
        print('You lose!')
        losses = losses + 1
    elif Player_input == 's' and computermove == 'r':
        print('You lose!')
        losses = losses + 1
