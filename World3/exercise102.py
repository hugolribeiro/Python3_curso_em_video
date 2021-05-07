# Make a program that has a function factorial() that will receive two parameters:
# the first will indicate a number and the another named show() will be logic value (optional) indicating if
# will be show ou not the calculate process.

# Programmer: Hugo Leça Ribeiro

def factorial(number, show=False):
    result = 1
    for count in range(number, 0, -1):
        result *= count
        if show:
            if count > 1:
                print(f'{count} X ', end='')
            elif count == 1:
                print(f'{count} = ', end='')
    return result


# Main Program
print(factorial(6, True))
