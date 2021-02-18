# Exercise 004: Dissecting a variable
# Make a program that read something of the keyboard.
# Print in the screen your primitive type and all possible information about it.

something = input('Input here something: ')
print(f'Type: {type(something)}')
print(f'Length: {len(something)}')
print(f'Is a number? {something.isnumeric()}')
print(f'Is alphanumeric? {something.isalnum()}')
print(f'Is alphabetic? {something.isalpha()}')
print(f'Is blank spaces? {something.isspace()}')
