# Exercise 087: More than matrix in python
# Upgrade the previous version (exercise 086), showing:
# A) The sum of all even values inputted
# B) The sum of the values of the third column
# C) The highest value in the second line

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_even = 0
sum_third_column = 0
for line in range(0, 3):
    for column in range(0, 3):
        number = int(input(f'Input here the number of the {line} line and {column} column: '))
        matrix[line][column] = number
        if number % 2 == 0:
            sum_even += number
        if column == 2:
            sum_third_column += number

for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[line][column]:^5}]', end='')
    print()
print(f'The sum of all even numbers: {sum_even} ')
print(f'The sum of all values in third column: {sum_third_column}')
print(f'The highest value in the second line: {max(matrix[1])}')
