# Exercise 009: math table
# Make a program that read an any integer number and show its math table

number = int(input('Input here a number: '))

for multiply in range(0, 11):
    print(f'{number} X {multiply} = {number * multiply}')
