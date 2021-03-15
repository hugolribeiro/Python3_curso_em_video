# Exercise 066: Several numbers with flag
# Make a program that read several integers numbers.
# The program only will stop if the user input the value 999.
# At the end, show how many numbers was inputted and what was the sum of their.

_sum = 0
amount = 0
while True:
    number = int(input('Input here a number. \'999\' to stop: '))
    if number != 999:
        _sum += number
        amount += 1
    else:
        break
print(f'Amount numbers: {amount}\n'
      f'The sum of their is: {_sum}')
