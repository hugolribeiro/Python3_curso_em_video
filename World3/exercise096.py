# Objective: Make a program that have a function called Area().
# Receive the dimensions of a rectangular land (width and length) and show its area.
# Programmer: Hugo Leça Ribeiro


def area(width, length):
    amount_area = width * length
    print(f'The area of this land is equal than: {amount_area}m²')


width = float(input("Input here the width of this land (in meters): "))
length = float(input("Input here the length of this land (in meters): "))

area(width, length)
