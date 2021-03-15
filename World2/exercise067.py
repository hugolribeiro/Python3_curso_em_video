# Exercise 067: Multiplication table v3.0
# Make a program that shows the multiplication table of several numbers, one by one,
# for each value inputted by the user.
# The program will end when the number inputted was a negative number.

def multiplication_table(num):
    for multiplicador in range(0, 11):
        print(f'{num} X {multiplicador} = {num * multiplicador}')


while True:
    number = int(input('Input here a number. Negative number to stop the program. '))
    if number >= 0:
        multiplication_table(number)
        print('-=' * 20)
    else:
        print('Ending the program...')
        break
