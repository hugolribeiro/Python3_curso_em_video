# Objective: Make a program that read the name, sex and the age of several people, storage these datas in a dictionary.
# Storage all dictionaries in a list.
# At the end, show:
# A) How many people was registered.
# B) The average age of the group.
# C) The list with all women.
# D) A list with all people with age above the average.

# Programmer: Hugo Leça Ribeiro

person = dict()
people = list()
want_continue = True
while want_continue:
    value = False
    name = str(input('Name: '))
    sex = str(input('Sex: [M/F]')).upper()
    age = int(input('Age: '))
    person['Name'] = name
    person['Sex'] = sex
    person['Age'] = age
    people.append(person.copy())
    while not value:
        want_continue = str(input('Do you want to continue? [Y/N] '))
        if want_continue in ['Yes', 'YES', 'Y', 'y', 'yes']:
            want_continue = True
            value = True
        elif want_continue in ['No', 'no', 'n', 'N', 'NO']:
            want_continue = False
            value = True
        else:
            print('Sorry, wrong option. Try again.')
    person.clear()
print('-=' * 30)
amount_people = len(people)
total_age = 0
print(f'- The group have {amount_people} people.')
print('- The women registered was: ', end='')
for person in people:
    total_age += person.get('Age')
    if person.get('Sex') == 'F':
        print(f'{person.get("Name")}', end=';  ')
average_age = total_age / amount_people
print(f'\n- The average age is: {average_age}')
print('\- The list of people that are above the average is: \n')
for person in people:
    if person.get('Age') > average_age:
        print(f'Name = {person.get("Name")}', end='   ')
        print(f'Sex = {person.get("Sex")};', end='   ')
        print(f'Age = {person.get("Age")};\n')
print('<< FINISHED >>')
