# Exercise 035: Checking a triangle v1.0
# Make a program that read the length of three lines and tell to the user whether or not they form a triangle.

print('=' * 20)
print('Checking a triangle')
print('=' * 20)

line1 = float(input('First line: '))
line2 = float(input('Second line: '))
line3 = float(input('Third line: '))

if line1 < line2 + line3 and line2 < line1 + line3 and line3 < line1 + line2:
    print('The lines above can form a triangle!')
else:
    print('The lines above cannot form a triangle!')
