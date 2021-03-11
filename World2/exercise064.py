# Exercise 064: Treating several values v1.0
# Make a program that reads several integers numbers.
# The program will only be interrupted when the user enters the value 999.
# At the end, show how many numbers were inputted and what was their sum.

number = int(input('Input here a number: '))
_sum = 0
count = 0
while number != 999:
    _sum += number
    count += 1
    number= int(input('Input another number here: '))

print('\nFinished the program!\n'
      f'At the total we got {count} numbers\n'
      f'Their sum is equal to: {_sum}')
