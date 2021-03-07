# Exercise 046: countdown
# Make a program that shows on the screen a countdown to the fireworks.
# It will begin in 10 to 0, with a break of 1 second between the numbers.

from time import sleep

for count in range(10, -1, -1):
    print(f'{count}...')
    sleep(1)
print('BOOOMM')
