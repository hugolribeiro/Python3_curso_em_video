# Exercise 065: Higher and Lower values
# Make a program that read several integers numbers.
# At the end, show the average between all values, and tell which was the higher and the lower values.
# The program must ask to the user if he wants or not to continue to input values.

higher = 0
lower = 0
_sum = 0
average = 0
amount = 0
answer = 'Y'

while answer == 'Y':
    number = int(input('Input here a number: '))
    _sum += number
    amount += 1
    if amount == 1:
        higher = lower = number
    else:
        if number > higher:
            higher = number
        if number < lower:
            lower = number
    answer = input("Do you want do continue?\n"
                   "\n[Y] - Yes"
                   "\n[N] - No\n").upper()
average = _sum / amount
print(f'You inputted {amount} numbers and the average was {average}')
print(f'The higher number was: {higher}. The lower number was: {lower}')
