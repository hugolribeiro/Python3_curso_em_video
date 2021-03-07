# Exercise 048: Sum of odds multiples of three
# Make a program that calculates the sum of all even numbers that are multiple of three and are between 1 and 500.

sum_ = 0
for number in range(1, 501, 2):
    if number % 3 == 0:
        sum_ += number
print(sum_)
