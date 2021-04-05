# Exercise 080: Sorted list without repetitions
# Make a program where the user can input five numeric values and register them into a list
# Input these values in correct index (without use sort()). At the end, show and ordered list on the screen.

numbers_list = []

for numbers in range(0, 5):
    actual_number = int(input('Input here a number: '))
    if numbers == 0 or actual_number > numbers_list[-1]:
        numbers_list.append(actual_number)
    else:
        pos = 0
        while pos < len(numbers_list):
            if actual_number <= numbers_list[pos]:
                numbers_list.insert(pos, actual_number)
                break
            pos += 1
print(numbers_list)
