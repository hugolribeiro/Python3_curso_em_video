# Exercise 019: Drawing an item in a list
# A teacher want to draw one of your four students to erase the board.
# Make a program that helps he, so will read the name of the students and will print the name chosen.

import random

students = []
for student in range(1, 5):
    students.append(input(f'Input here the name of the student number {student}: '))

chosen_student = random.choice(students)
print(f'The chosen student was: {chosen_student}')
