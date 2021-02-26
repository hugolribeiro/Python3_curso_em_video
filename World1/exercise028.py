# Exercise 028: Guest game v1.0
# Make a program that makes the computer "think" in an integer number between 0 and 5
# And ask the user to try to find out which number was the chosen number.
# The program must write on the screen whether the user won or lost.

from random import randint
from time import sleep

print('Hello, I will think in a number between 0 and 5. Try to fin out this!')
sleep(1)
print('Thinking...')
sleep(2)
chosen_number = randint(0, 5)
user_choice = int(input('Please, input a number between 0 and 5: '))

if user_choice == chosen_number:
    print(f'Wowww, you won! The number was: {chosen_number}')
else:
    print(f'You lost!! The number was: {chosen_number}')
