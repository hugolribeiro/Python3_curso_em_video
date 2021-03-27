# Exercise 074: Highest and Lowest values in a tuple
# Make a program that will generate random numbers and will put them into a tuple.
# After this, show a list of these numbers, show the highest and the lowest number.

from random import randint

random_numbers = tuple(randint(0, 50) for _ in range(5))

print(f'The numbers chosen were: {random_numbers}\n'
      f'The highest number was: {max(random_numbers)}\n'
      f'The lowest number was: {min(random_numbers)}')
