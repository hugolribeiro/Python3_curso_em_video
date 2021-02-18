# Exercise 010: currency converter
# Make a program that read how much money a person has in their wallet.
# Show how much dollars he can buy
# Consider U$ 1,00 = R$ 3,27

money = float(input('Input here how much money do you have: '))
DOLLARS = 3.27
money_dollars = money / DOLLARS

print(f'You can buy {money_dollars:.2f} dollars.')
"""
EXERCÍCIO 010: Conversor de Moedas
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.
Considere U$ 1,00 = R$ 3,27
"""