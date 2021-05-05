# Make a program that have the function named vow() that will receive how parameter the birth year of a person.
# Will return a literal value that will say if a person have the vow Negate, Optional or mandatory at the elections.

# Programmer: Hugo Leça Ribeiro

from datetime import date


def vow(b_year):
    actual_year = date.today().year
    age = actual_year - b_year
    if 18 <= age < 65:
        return f'With {age} years: MANDATORY VOW'
    elif age >= 16 or age >= 65:
        return f'With {age} years: OPTIONAL VOW'
    elif age < 16:
        return f'With {age} years: NEGATE VOW'


print('-' * 20)
birth_year = int(input('Birth Year: '))
print(vow(birth_year))
