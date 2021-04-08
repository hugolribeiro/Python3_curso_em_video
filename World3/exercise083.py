# Exercise 083: Validating Maths Expressions
# Make a program where the user input an expression that use parenthesis.
# Your application must analyze if the expression is with the parenthesis opened or closed and in the correct order.

expression = input('Input here your expression: ')
stack = []
for character in expression:
    if character == '(':
        stack.append('(')
    elif character == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break
if len(stack) == 0:
    print('Your expression is valid')
else:
    print('Your expression is invalid')
