# Exercise 008: measures convertor
# make a program that read a value in meters and print it converted in centimeters and millimeters

value = float(input('Value in meters: '))
value_cm = value * 100
value_mm = value * 1000

print(f'The value {value} meters is equal than:\n'
      f'{value_cm} centimeters\n'
      f'{value_mm} millimeters')

"""
EXERCÍCIO 008: Conversor de Medidas
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""