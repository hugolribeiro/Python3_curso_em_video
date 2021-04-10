# Exercise 084: Full list and data analyze
# Make a program that reads the name and weight of several people, storage them into a list.
# At the end show:
# A) How mane people have been registered
# B) The heavier person
# C) The lighter person.

want_continue = 'Y'
people = []
while want_continue != 'N':
    name = input('Name: ')
    weight = float(input('Weight: '))
    people.append((name, weight))
    want_continue = input('Want to continue?\n'
                          '[N] to end the program\n').upper()
print(f'Was registered {len(people)} people')
print(f'The heavier person is:\n'
      f'Name: {max(people, key=lambda person: person[1])[0]}\n'
      f'Weight: {max(people, key=lambda person: person[1])[1]}')
print(f'The lighter person is:\n'
      f'Name: {min(people, key=lambda person: person[1])[0]}\n'
      f'Weight: {min(people, key=lambda person: person[1])[1]}')
