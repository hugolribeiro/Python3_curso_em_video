# Exercise 089: Banknotes with nested lists
# Author: Hugo Leça Ribeiro
# Make a program that reads the name and two scores of several students
# Storage all data into a nested list
# At the end, show the banknotes that contains the average score of each student
# and allow to show the scores of each student.

bank_notes = []
amount_students = int(input('How many students? '))

for student in range(amount_students):
    student_data = [
        input(f'Name of the {student + 1}º student: '), [float(input('First score: ')), float(input('Second score: '))
                                                         ]]
    bank_notes.append(student_data)
    print('-' * 30)

for student in bank_notes:
    print(f'{student[0]}\'s average score: {sum(student[1]) / 2}')
    print(f'Individual scores: {student[1]}')
    print('-' * 30)
