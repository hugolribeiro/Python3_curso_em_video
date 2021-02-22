# Exercise 023: Splitting the number digits
# Make a program that read a number between 0 and 9999, show in the screen each of the digits splitted.

# Example: number 1834
# Unity: 4
# Tens: 3
# hundred: 8
# thousands: 1

inputted_number = int(input('Input here a number between 0 and 9999: '))
calc_number = inputted_number
thousands = calc_number // 1000
calc_number -= thousands * 1000
hundred = calc_number // 100
calc_number -= hundred * 100
tens = calc_number // 10
calc_number -= tens * 10
unity = calc_number

print(f'Number: {inputted_number}\n'
      f'Thousands: {thousands}\n'
      f'Hundred: {hundred}\n'
      f'Tens: {tens}\n'
      f'Unity: {unity}')