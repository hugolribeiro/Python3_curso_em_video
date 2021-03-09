# Exercise 054: Adulthood group
# Make a program that reads the year of birth of seven people.
# At the end, show how many people have not yet reached adulthood and how many have reached this.
from datetime import date

today = date.today().year
print(today, type(today))
amount_adulthood = 0
amount_not_adulthood = 0
for person in range(1, 8):
    birth_year = int(input(f'{person}º birth year: '))
    age = today - birth_year
    if age >= 18:
        amount_adulthood += 1
    else:
        amount_not_adulthood += 1

print(f'We have {amount_adulthood} adults in this group\n'
      f'We have {amount_not_adulthood} not adults in this group')
