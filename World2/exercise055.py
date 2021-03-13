# Exercise 055: Highest and Lowest of the sequence
# Make a program that reads the weight of five people.
# At the end, show which was the highest and the lowest weight inputted.

highest = 0
lowest = 0
for person in range(1, 6):
    weight = float(input(f'{person}º person\'s weight: '))
    if person == 1:
        highest = weight
        lowest = weight
    else:
        if weight > highest:
            highest = weight
        elif weight < lowest:
            lowest = weight

print(f'The highest weight was: {highest}\n'
      f'The lowest weight was: {lowest}')
