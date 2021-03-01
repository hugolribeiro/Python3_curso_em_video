# Exercise 034: multiples raises
# Write a program that ask the employee's income and calculate the raise value
# To the incomes higher than R$ 1250.00 raise it in 10%
# To incomes lower or equal, the raise is by 15%

employee_income = float(input('Input here the emplyee\'s income: '))

raised_value = employee_income * 1.1 if employee_income > 1250 else employee_income * 1.15
print(f'The employee\'s income raised is equal than {raised_value}')
