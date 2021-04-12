# Exercise 085: List with even and odd numbers
# Make a program that the user input seven numeric values and register them into a unique list.
# That list will keep separated the odd and even numbers.
# At the end, show the odd and even values in crescent order.

# numbers = [[even], [odd]]
numbers = [[], []]

for amount in range(0, 7):
    number = int(input('Input here a number: '))
    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)
print(f'Even numbers: {sorted(numbers[0])}')
print(f'Odd numbers: {sorted(numbers[1])}')
