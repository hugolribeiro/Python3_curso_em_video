# Exercise 038: Comparing numbers
# Write a program that read two integers numbers and compare them, showing in the screen a message:
# - The first value is the highest
# - The second value is the highest
# - Don't exist a highest value, both are equals

first = int(input('First number: '))
second = int(input('Second number: '))

if first > second:
    print(f'The first value ({first}) is higher than the second value ({second})')
elif second > first:
    print(f'The second value ({second}) is higher than the first value ({first})')
else:
    print(f'Don\'t exist a highest value, both are equals')
