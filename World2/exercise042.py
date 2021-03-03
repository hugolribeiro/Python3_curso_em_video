# Exercise 042: Analyzing triangles v2.0
# Remake the exercise 035, increase the resource to show the triangle type:
# - Equilateral: has three equal sides
# - Isosceles: has exactly two equal sides
# - Scalene: has three different angles and none of its sides are equal in length

print('=' * 20)
print('Checking a triangle')
print('=' * 20)

line1 = float(input('First line: '))
line2 = float(input('Second line: '))
line3 = float(input('Third line: '))

if line1 < line2 + line3 and line2 < line1 + line3 and line3 < line1 + line2:
    print('The lines above can form a triangle!')
    if line1 == line2 == line3:
        print('EQUILATERAL')
    elif line1 != line2 != line3 != line1:
        print('SCALENE')
    else:
        print('ISOSCELES')
else:
    print('The lines above cannot form a triangle!')
