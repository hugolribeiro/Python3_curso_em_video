# Exercise 051: Arithmetic Progression
# Make a program that read the first term and the common difference of an Arithmetic Progression.
# At the end, show the firsts 10 terms of this Progression.


first_term = int(input('First term: '))
common_difference = int(input('Common difference: '))
last_term = first_term + (common_difference * 10)
for term in range(first_term, last_term, common_difference):
    print(term)
