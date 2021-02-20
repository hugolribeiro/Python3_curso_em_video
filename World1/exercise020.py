# Exercise 020: Drawing an order in a list
# The same teacher of the before exercise want to raffle the presentation order of the students work.
# Make a program that read the name of four students and print in the draw order.

import random

students = []
for student in range(1, 5):
    students.append(input(f'Input here the name of the student number {student}: '))
random.shuffle(students)

print(f'The raffled order was: {students}')
