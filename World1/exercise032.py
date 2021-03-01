# Exercise 032: Leap year
# Make a program that read any year and show if it is a leap year.

year = int(input('Input here a number: '))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f'The year {year} is a leap year!')
else:
    print(f'The year {year} ins\'t a leap year!')
