# Exercise 018: sine, cosine, tangent
# Make a program that read an any angle and show in the screen the value of the sine, cosine and tangent of this angle.
import math

angle = float(input('Input here a angle: '))
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))

print(f'sine = {sine}\n'
      f'cosine = {cosine}\n'
      f'tangent = {tangent}')
"""
EXERCÍCIO 018: Seno, Cosseno e Tangente
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""