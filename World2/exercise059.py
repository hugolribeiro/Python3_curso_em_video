# Exercise 059: Making an options menu
# Make a program that read two values and show the menu like the below:
# [1] Sum
# [2] Multiply
# [3] Higher
# [4] New numbers
# [5] Exit the program
# Your program must realize the requested operation in each case.

from time import sleep

print('You will need to choose two numbers')
number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))
option = 0
while option != 5:
    option = input('Please, choose one of these options:\n'
                       '[1] - Sum\n'
                       '[2] - Multiply\n'
                       '[3] - Higher\n'
                       '[4] - New numbers\n'
                       '[5] - Exit the program\n')
    if option == '1':
        print(f'The sum of {number1} and {number2} is: {number1 + number2}')
    elif option == '2':
        print(f'{number1} X {number2} = {number1 * number2}')
    elif option == '3':
        print(f'The higher number is: {max(number1, number2)}')
    elif option == '4':
        number1 = int(input('Number 1: '))
        number2 = int(input('Number 2: '))
    elif option == '5':
        print('Finishing...')
    else:
        print('Wrong option!')
        print('=-' * 20)
print('Goodbye')
