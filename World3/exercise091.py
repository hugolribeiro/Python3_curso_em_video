# Author: Hugo Leça Ribeiro
# Exercise 091: Dice game in Python
# Make a program where four players play a dice and get random results.
# Storage these results in a dictionary.
# At the end, put the dictionary in order (highest value first).

from random import randint
from operator import itemgetter

results = {
    'Player1': randint(1, 6),
    'Player2': randint(1, 6),
    'Player3': randint(1, 6),
    'Player4': randint(1, 6)
}

print('Sorted values')
for key, value in results.items():
    print(f'The {key} gets {value} at the roll')

print('-' * 30)
print('The winners:')
ranking = sorted(results.items(), key=itemgetter(1), reverse=True)
for key, value in enumerate(ranking):
    print(f'{key+1}º - {value[0]} rolled {value[1]}')
