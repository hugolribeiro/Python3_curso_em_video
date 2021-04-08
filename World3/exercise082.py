# Exercise 082: Dividing values into several lists
# Make a program that reads several numbers and put them into a list.
# After that, make two extras lists that contains only evens numbers and odds numbers inputted, respectively.
# At the end, show the contents of the three lists.

all_numbers = []

want_continue = 'Y'

while want_continue != 'N':
    actual_number = int(input('Input here a number: '))
    all_numbers.append(actual_number)
    want_continue = input('Do you want to continue?\n'
                          '[N] to exit').upper()
even_numbers = []
odd_numbers = []
for number in all_numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print(f'All numbers: {all_numbers}')
print(f'Odd numbers: {odd_numbers}')
print(f'Even numbers: {even_numbers}')
