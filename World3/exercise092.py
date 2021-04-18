# Objective: Make a program that read the name, birth year and the CTPS and storage them (with the age) in a dictionary.abs
# If the CTPS was different by ZERO, the dictionary will receive the hire year and the income.
# Calculate and add, besides the age, how many years the person will retire. (with 35 years the person retire)

# Programmer: Hugo Leça Ribeiro

from datetime import date

person = dict()
name = str(input('Name: '))
birth_year = int(input('Birth Year: '))
ctps = int(input('CTPS: '))
person['Name'] = name
year = date.today().year
actual_age = year - birth_year
person['Age'] = actual_age
person['CTPS'] = ctps
if ctps != 0:
    hire_year = int(input('Hire Year: '))
    income = float(input('Income: R$ '))
    person['Hire Year'] = hire_year
    person['Income'] = income
    time_worked = year - hire_year
    will_retire = 35 - time_worked
    if will_retire <= 0:
        will_retire = 'You already can retire, enjoy it.'
    person['Retire'] = will_retire

print('-=' * 40)
print(person)
for key, value in person.items():
    print(f'{key} have the value: {value}')
