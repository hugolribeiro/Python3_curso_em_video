# Make a program that has the function named readint(),
# that will works similar to the function input(), but it will do the validation to accept only one numeric value.
# Example: n = readint('Input a number n')


def readint():
    while 1:
        maybe_number = input('Input here a number: ')
        if maybe_number.isnumeric():
            number = int(maybe_number)
            return number
        else:
            print('\033[0;31mError! Input an integer number.\033[m')


int_number = readint()
print(f'The number inputted was: {int_number}')
