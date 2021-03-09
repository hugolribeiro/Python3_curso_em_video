# Exercise 057: Data validation
# Make a program that reads the sex of a person, but only accept the values 'M' or 'F'.
# If the input is wrong, ask for input it again until have a valid value.

sex = input('[M] or [F]: ').strip()
while sex not in 'MF':
    print('Sorry, wrong input.')
    sex = input('[M] or [F]: ')
print(f'Sex received successfully. Sex: {sex}')
