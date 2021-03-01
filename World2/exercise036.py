# Exercise 036: Approving loan
# Write a program to approve the bank loan for the purchase a home.
# Ask the value of the house, the employee's income and how many years he will pay.
# The monthly installment cannot exceed 30% of the revenue, or the loan will be denied.


house_value = float(input('What is the house value? '))
employee_income = float(input('Employee\'s income: '))
many_years = int(input('How many years you will pay? '))
amount_months = many_years * 12

if house_value / amount_months > (0.3 * employee_income):
    print('Sorry, but the loan will be denied!')
else:
    print('The loan will be accept!')
