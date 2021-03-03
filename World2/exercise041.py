# Exercise 041: Classifying athletes
# The Swimming National Confederation need a program that read the birth year of an athlete and show his category
# According his age:
# - Up to 9 years old: Little
# - Up to 14 years old: Childish
# - Up to 19 years old: Junior
# - Up to 25 years old: Senior
# - Above than 25 years old: Master

from datetime import date
actual = date.today().year
athlete_birth_year = int(input('Athlete birth year: '))
athlete_age = actual - athlete_birth_year

if athlete_age <= 9:
    print(f'Category: Little')
elif athlete_age <= 14:
    print(f'Category: Childish')
elif athlete_age <= 19:
    print(f'Category: Junior')
elif athlete_age <= 25:
    print(f'Category: Senior')
else:
    print('Category: Master')
