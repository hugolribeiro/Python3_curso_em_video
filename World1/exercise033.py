# Exercise 033: Higher and Lower values
# Make a program that read three numbers and show which is the higher and which is the lower value.

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

# Checking which is the lowest value
lowest = a

if b < a and b < c:
    lowest = b
elif c < a and c < b:
    lowest = c

# Checking which is the highest value

highest = a

if b > a and b > c:
    highest = b
elif c > a and c > b:
    highest = c

print(f'The lowest value is: {lowest}\n'
      f'The highest value is: {highest}')
