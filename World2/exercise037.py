# Exercise 037: Numeric bases conversor
# Write a program that read an any integer number and ask to the user to chosen which will be the base to conversor:
# - 1 to binary
# - 2 to octal
# - 3 to hexadecimal

number = int(input('Input here a number: '))
base_option = int(input('Choose the base:\n'
                        '[1] to binary\n'
                        '[2] to octal\n'
                        '[3] to hexadecimal\n'))

if base_option == 1:
    print(f'The number {number} in binary is: {bin(number)}')
elif base_option == 2:
    print(f'The number {number} in octal is: {oct(number)}')
elif base_option == 3:
    print(f'The number {number} in hexadecimal is: {hex(number)}')
else:
    print(f'Wrong option, please, try again')
