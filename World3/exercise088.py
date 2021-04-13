# Author: Hugo Leça Ribeiro
# Exercise 088: Hints to lottery (Mega-Sena)
# Make a program that helps a lottery player to create Hints.
# The program will asks how many games will be generate and will draw 6 numbers between 1 and 60 to each game,
# registering all into a nested list.

from random import sample
from time import sleep

games_drawn = []
print('-' * 30)
print('   Hits to Mega Sena Game        ')
print('-' * 30)
amount_games = int(input('Input here how many games do you want to see: '))

for game in range(0, amount_games):
    print(f'\n        Game number {game+1}\n')
    actual_game = sorted(sample(list(range(1, 61)), 6))
    print(*actual_game, sep=' - ')
    games_drawn.append(actual_game)
    sleep(1)
    print('-' * 30)
