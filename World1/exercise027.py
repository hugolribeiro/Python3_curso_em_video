# Exercise 027: First and Last name of a person
# Make a program that read the person's full name, showing the first and the last name separately
# Example: Ana Maria de Souza
# First name = Ana
# Last name = Souza

full_name = input('Input here the full name: ').split()
first_name = full_name[0]
last_name = full_name[-1]
print(f'First name: {first_name}\n'
      f'Last nam: {last_name}')
