# Rock-paper-scissors
# Make a program that plays rock-paper-scissors with you

from random import choice
from time import sleep

itens = ['rock', 'paper', 'scissor']
computer_choice = choice(itens)
print('Your options:\n'
      '[0] - Rock\n'
      '[1] - Paper\n'
      '[2] - Scissor')
player_choice = itens[int(input('What is your choice?\n'))]
print('ROCK')
sleep(1)
print('PAPER')
sleep(1)
print('SCISSORS')
sleep(1)
print('-=' * 15)
print(f'The computer plays {computer_choice}')
print(f'The player plays {player_choice}')
print('-=' * 15)
if computer_choice == 'rock':
    if player_choice == 'rock':
        print('DRAW!')
    elif player_choice == 'paper':
        print('Player wins')
    else:
        print('Computer wins')
elif computer_choice == 'paper':
    if player_choice == 'rock':
        print('Computer wins')
    elif player_choice == 'paper':
        print('DRAW')
    else:
        print('Player wins')
else:
    if player_choice == 'rock':
        print('Player wins')
    elif player_choice == 'paper':
        print('Computer wins')
    else:
        print('DRAW!')
