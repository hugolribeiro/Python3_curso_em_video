# Exercise 015: Car rent
# Write a program that ask the amount of km traveled by a rented car and
# the amount of days that it was rent. Calculate the price to pay,
# knowing that car cost R$ 60 per day and R$ 0,15 per km traveled.

km_traveled = float(input('Input here the amount of km traveled: '))
amount_days = int(input('Input here the amount of days: '))

total_price = 60 * amount_days + 0.15 * km_traveled

print('You need to pay the amount of R${:.2f}'.format(total_price))
