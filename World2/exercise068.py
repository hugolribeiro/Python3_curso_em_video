# Exercise 068: Odds and evens game
# Make a program that plays odds and evens with the computer.
# The game only will interrupted when the player Lose.
# Show the amount of consecutive victories.
from random import randint

lose = False
amount_victories = 0
while not lose:
    print('Well, let\'s play another match')
    user_choice = int(input('Input here a value between 0 and 10: '))
    computer_choice = randint(0, 10)
    total_choice = user_choice + computer_choice
    odd_or_even = ' '
    while odd_or_even not in 'OE':
        odd_or_even = input('You choose ODD or EVEN?\n'
                            '[O] - ODD\n'
                            '[E] - EVEN\n').strip().upper()[0]
    print(f'The computer choice the number {computer_choice}. So we got the number {total_choice}')
    if total_choice % 2 == 0:
        if odd_or_even == 'E':
            print('You win!')
            amount_victories += 1
        else:
            print('You loose')
            lose = True
    else:
        if odd_or_even == 'O':
            print('You win!')
            amount_victories += 1
        else:
            print('You loose')
            lose = True

print(f'You won {amount_victories} times!')
