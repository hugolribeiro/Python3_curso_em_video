# Exercise 075: checking the data of a tuple
# Develop a program that read four values and storage them into a tuple.
# At the end, show:
# A) How many times appears the value 9
# B) In which index was inputted the first value 3
# C) What were the even numbers

main_tuple = (int(input(f'Input here the 1º number: ')),
             int(input(f'Input here the 2º number: ')),
             int(input(f'Input here the 3º number: ')),
             int(input(f'Input here the 4º number: ')))


print(f'The number 9 appeared {main_tuple.count(9)} times')
if 3 in main_tuple:
    print(f'The number three was inputted at the index number {main_tuple.index(3)}')
for number in main_tuple:
    if number % 2 == 0:
        print(number, end=' ')
