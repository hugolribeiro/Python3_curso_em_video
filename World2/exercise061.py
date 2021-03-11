# Exercise 061: Arithmetic Progression v2.0
# Remake the exercise 051, read the first term and the common difference of a Progression Arithmetic.
# Show the firsts ten terms using the while structure

first_term = int(input('First term: '))
common_difference = int(input('Common difference: '))

term = 1
actual_term = first_term
while term <= 10:
    print(actual_term, end=' ')
    term += 1
    actual_term += common_difference
