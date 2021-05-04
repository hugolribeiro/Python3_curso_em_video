# Objective: Make a program that have a function 'highest', that will receive several parameters with integers values.
# It program must analyze all the values and tell which them is the highest.

# Programmer: Hugo Leça Ribeiro
from time import sleep


def highest(*numbers):
    print('-=' * 20)
    print('Analysing the values...')
    for number in numbers:
        print(f'{number}', end=' ', flush=True)
        sleep(1)
    if len(numbers) > 0:
        print(f'Was inputted {len(numbers)} values.')
        highest_number = max(numbers)
        print(f'The highest number is: {highest_number}')
    else:
        print('Was inputted 0 values.')


highest(2, 9, 4, 5, 7, 1)
highest(4, 7, 0)
highest(1, 2)
highest(6)
highest()
