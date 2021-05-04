# Objective: Make a program that have a list named numbers and two functions named randnumbers and sumeven.
# The first function will generate 5 random numbers and will put it in a list.
# The second function will sum only the even numbers in this list and will show the sum.

# Programmer: Hugo Leça Ribeiro

from random import randint


def randnumbers():
    numbers = list()
    for i in range(0, 5):
        numbers.append(randint(0, 20))
    print(numbers)
    return numbers


def sumeven(numbers):
    sum_evens = 0
    for number in numbers:
        if number % 2 == 0:
            sum_evens += number
    print(f'The sum of the even numbers is: {sum_evens}')


numbers = randnumbers()
sumeven(numbers)
