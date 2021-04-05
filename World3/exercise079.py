# Exercise 079: Unique values in a list
# Make a program where the user can input several numerical values
# register them into a list.
# If a number is already in it list, it won't be add.
# At the end, show all unique values inputted, in ascending order.

unique_values = []

while True:
    number = int(input('Input here a number: \n'
                       '(type 999 to stop)    '))
    if number == 999:
        break
    if number in unique_values:
        print('Sorry, this number is already in list')
    else:
        unique_values.append(number)
        print(f'Number {number} added successfully')
print(sorted(unique_values))
