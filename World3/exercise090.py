# Author: Hugo Leça Ribeiro
# Exercise 090: Dictionary in Python
# Make a program that reads the name and average score of a student
# Storage too the situation in a dictionary
# At the end, show the contain

student = dict()

student['Name'] = input('Name: ')
student['Average'] = float(input(f'Average of the student {student["Name"]}: '))
if student['Average'] >= 7:
    student['Status'] = 'Approved'
elif 3 <= student['Average'] < 7:
    student['Status'] = 'Recovery'
else:
    student['Status'] = 'Reproved'
print('-' * 30)
for key, value in student.items():
    print(f'{key} : {value}')
