# Exercise 011: Painting the wall
# Make a program that read the width and the height of a wall in meters.
# Calculate its area and the amount of paint needed to paint it.
# You know that each liter of paint is used to paint an area of 2m²

width = float(input('Input here the width: '))
height = float(input('Input here the height: '))
area = width * height

amount_of_paint = area / 2

print(f'The amount of paint that will be need is: {amount_of_paint} liters')
