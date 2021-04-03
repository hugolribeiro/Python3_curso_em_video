# Exercise 078: Highest and Lowest values in a list
# Make a program that reads 5 numerical values and stores them   in a list.
# At the end, show which was the highest and the lowest values inputted and its respective positions in this list.

numbers_list = []

for index in range(0, 5):
    number = int(input('Input here a number: '))
    numbers_list.append(number)

highest_value = max(numbers_list)
lowest_value = min(numbers_list)
print(f'Highest value = {highest_value} at the {numbers_list.index(highest_value)+1}º position')
print(f'Lowest value = {lowest_value} at the {numbers_list.index(lowest_value)+1}º position ')
