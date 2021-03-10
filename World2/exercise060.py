# Exercise 060: Factorial calculation
# Make a program that read any number and show its factorial
# Example: 5! = 5 X 4 X 3 X 2 X 1 = 120

number = int(input('Input here a number: '))
factorial = 1
print(f'{number}! = ', end='')
for multiply in range(number, 0, -1):
    factorial = multiply * factorial
    print(f'{multiply}', end='')
    print(' X ' if multiply > 1 else ' = ', end='')
print(factorial)

