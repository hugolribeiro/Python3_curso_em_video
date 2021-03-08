# Exercise 049: Math table v2.0
# Remake the exercise 009, showing the math table of a number that the user choice, but now use a loop for this

number = int(input('Number: '))
for multiply in range(0, 11, 1):
    print(f'{number} X {multiply} = {number * multiply}')
