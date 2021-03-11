# Exercise 062: Super Arithmetic Progression v3.0
# Improve the exercise 061, ask the user if he wants to show more terms.
# The program will finish when the user says he wants to show 0 terms.

first_term = int(input('First term: '))
common_difference = int(input('Common difference: '))
number_terms = int(input('How many terms wanna see? '))
actual_term = first_term
while number_terms > 0:
    counter = 1
    while counter <= number_terms:
        print(actual_term, end=' ')
        actual_term += common_difference
        counter += 1
    number_terms = int(input('\nDo you want to insert more terms? How many?\n'
                             '[0] - to finish the program\n'))
print('FINISHED')
