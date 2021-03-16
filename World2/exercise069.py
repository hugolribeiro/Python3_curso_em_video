# Exercise 069: Data group analyze
# Make a program that reads the age and the sex of severa people.
# For each person registered, the program will ask if the want or not to continue.
# At the end, show:
# A) How many people are over than 18 years old.
# B) How many men was registered
# C) How many women are under than 20 years old.

overthan18 = 0
amount_men = 0
women_under20 = 0
another_person = True
while another_person:
    person_sex = input('[M] - Male\n'
                       '[F] - Female\n').strip().upper()
    person_age = int(input('Age: '))
    if person_age > 18:
        overthan18 += 1
    if person_sex == 'M':
        amount_men += 1
    elif person_age < 20:
        women_under20 += 1
    another_person = input('Do you want to register another person?\n'
                           '[Y] - Yes\n'
                           '[N] - No\n').strip().upper()
    if another_person == 'N':
        another_person = False
print(f'A : {overthan18} people over than 18 years old\n'
      f'B : {amount_men} men\n'
      f'C : {women_under20} women under than 20 years old')
