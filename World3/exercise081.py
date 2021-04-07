# Exercise 081: Extracting data from a lista
# Make a program that reads several numbers and put them into a list. After that, show:
# A) How many numbers were inputted
# B) The numbers list, in descending order
# C) If the value 5 is in the list

numbers_list = []
want_continue = 'Y'
while want_continue != 'N':
    number = int(input('Input here a number: '))
    numbers_list.append(number)
    print(f'The number {number} was add into the list')
    want_continue = input('Do you want to continue?\n'
                          '[N] to stop the program\n').upper()
print(f'You inputted {len(numbers_list)} numbers')
print(f'The list in descending order: {sorted(numbers_list, reverse=True)}')
if 5 in numbers_list:
    print('The number 5 is in the list')
else:
    print('The number 5 ins\'t in the list')
