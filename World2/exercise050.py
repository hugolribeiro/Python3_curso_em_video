# Exercise 050: evens sum
# Develop a program that read six integers numbers and show the sum those who are evens.
# If the value is odd, disregard it.

_sum = 0
amount_evens = 0
for time in range(1, 7):
    number = int(input(f'Input the {time}º number: '))
    if number % 2 == 0:
        _sum += number
        amount_evens += 1
print(f'You inputted {amount_evens} even numbers. The sum of them is: {_sum}')
