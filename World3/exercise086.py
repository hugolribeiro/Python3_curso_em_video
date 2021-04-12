# Exercise 086: Matrix in Python
# Make a program that create a 3x3 matrix and fill it with inputted values.
# At the end, show the matrix with the correct format

matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for line in range(0, 3):
    for column in range(0, 3):
        matrix[line][column] = int(input(f'Input here a number to line {line} and column {column}: '))

for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[line][column]:^5}]', end='')
    print()
