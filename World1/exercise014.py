# Exercise 014: Temperature converter
# Read a program that convert an inputted temperature in ºC to ºF

temperature_c = float(input('Input here the temperature in ºC: '))
temperature_f = (temperature_c * 9/5) + 32

print(f'The temperature in Fahrenheit is: {temperature_f}')
