# Exercise 058: Guess game v2.0
# Better the game of the exercise 028 where the computer will "think" of a number between 0 and 10.
# But now the player will try to guess until he gets it right, showing in the the end how many guesses
# it took to win.

from random import randint
from time import sleep
print('-----The game is started-----')
print('The computer will think in a number between 0 and 10')
sleep(1)
print('Thinking...')
sleep(1)
computer_choice = randint(0, 10)
print('Ok, I got it\n'
      'Now try to guess')
sleep(1)
hit = False
guesses = 0
while not hit:
    player_choice = int(input('Input here a number between 0 and 10: '))
    guesses += 1
    if player_choice == computer_choice:
        print(f'Wowww, you got it with {guesses} guesses')
        hit = True
    else:
        print('Nah, you missed. Try it again!')
