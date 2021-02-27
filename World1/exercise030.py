# Exercise 030: Even or odd?
# Make a program that read an integer number and show if it is even or odd.

number = int(input('Input here a number: '))
if number % 2 == 0:
    print(f'The number {number} is an even number.')
else:
    print(f'The number {number} is an odd number.')