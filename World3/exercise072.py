# Exercise 072: Number in full
# Make a program that has a tuple completely filled with a number in the full counter, from zero to twenty.
# Your program must read a number (between 0 and 20) and show it in full.

numbers_in_full = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                   'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                   'nineteen', 'twenty')
number = -1
while number < 0 or number > 20:
    number = int(input('Input here a number between zero and twenty: '))

print(f'You inputted the number {numbers_in_full[number]}')
