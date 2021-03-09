# Exercise 056: Full analyzer
# Make a program that reads the name, age and sex of four people.
# At the end, show:
# - The average of age of the group.
# - What is the name of the older man.
# - How many women are under 20 years old.

average_age = 0
older_man_age = 0
older_man_name = ''
women_under_twenty = 0
total_age = 0

for person in range(1, 5):
    print(f'--------Information of the {person}º person----------')
    name = input('Name: ')
    age = int(input('Age: '))
    sex = input(f'[M] for male\n'
                f'[F] for female\n')
    total_age += age
    if sex == 'M' and age > older_man_age:
        older_man_age = age
        older_man_name = name
    if sex == 'F' and age < 20:
        women_under_twenty += 1
average_age = total_age / 4

print(f'The average age is: {average_age}')
print(f'The name of the older man is: {older_man_name} with {older_man_age} years old')
print(f'We have {women_under_twenty} women under 20 years old')
