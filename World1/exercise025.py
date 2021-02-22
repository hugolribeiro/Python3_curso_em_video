# Exercise 025: Searching a string inside of another string
# Make a program that read the name of a person and tell if he has "SILVA" in the name.

name = input('Input here the person\'s name: ')

if 'SILVA' in name.upper():
    print(f'YES! Have SILVA in the name {name}')
else:
    print(f'Does\'t have SILVA in the name {name}')
