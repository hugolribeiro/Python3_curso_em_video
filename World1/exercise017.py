# Exercise 017: Sides and Hypotenuse

# Make a program that read the length of the opposite side and of the adjacent side of a rectangle triangle.
# Calculate and print the value of hypotenuse

opposite = float(input('Value of opposite side: '))
adjacent = float(input('Value of adjacent side: '))

hypotenuse = ((opposite ** 2) + (adjacent ** 2)) ** 0.5
print(f'The hypotenuse is: {hypotenuse}')
