# Military Enlistment
# Make a program that read the birthdate of a young guy and inform, accordingly with his age,
# if he is still going to enlist in the military, or if it is time to enlist,
# or if it has already passed enlistment time.
# Your program should also show how much time is left or past the deadline.

from datetime import date
actual = date.today().year
birthyear = int(input('Birth Year: '))
age = actual - birthyear
print(f'Who has born in {birthyear} has {age} years in {actual}')
if age == 18:
    print('You have to be enlistment immediately!')
elif age < 18:
    balance = 18 - age
    year = actual + balance
    print(f'You don\'t have 18 years old yet. Still left {balance} years to the enlistment')
else:
    balance = age - 18
    year = actual - balance
    print(f'You should have signed up {balance} years ago')
    print(f'Your enlistment was in {year}')
