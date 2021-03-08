# Exercise 052: Prime numbers
# Make a program that read an integer number and tell if it is or not a prime number.

def verify_prime(num):
    if num < 2 or (num % 2 == 0 and num != 2):
        return False
    else:
        square_root = int(num ** 0.5)
        for divisor in range(square_root, 2, -1):
            if num % divisor == 0:
                return False
    return True


number = int(input('Input here a number: '))
if verify_prime(number):
    print(f'The number {number} is a prime number')
else:
    print(f'The number {number} isn\'t a prime number')
