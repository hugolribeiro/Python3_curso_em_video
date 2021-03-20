# Exercise 071: ATM simulator
# Make a program that simulates the operation of an ATM.
# At the begin, ask to the user what value will be withdraw (an integer number)
# and the program will informs how many banknotes of each value will be give.
# Observation: Consider that the banking box has these banknotes: R$ 50, R$ 20, R$ 10, R$ 5, R$ 2.
# The minimum value to withdraw is R$ 5

c50 = 0
c20 =0
c10 = 0
c5 = 0
c2 = 0
value = 0
while value < 5:
    value = int(input('Input here value to withdraw: '))

while value % 5 != 0:
    value -= 2
    c2 += 1
c50 = value // 50
value -= c50 * 50
c20 = value // 20
value -= c20 * 20
c10 = value // 10
value -= c10 * 10
c5 = value // 5
value -= c5 * 5

print(f'{c50} banknotes of 50\n'
      f'{c20} banknotes of 20\n'
      f'{c10} banknotes of 10\n'
      f'{c5} banknotes of 5\n'
      f'{c2} banknotes of 2')
