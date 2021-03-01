# Exercise 031: Travel cost
# Make a program that ask the distance (in km) of a travel. Calculate the ticket price.
# The ticket will cost R$ 0,50 per km to travels of until 200km and R$ 0.45 to the travels more longest.

distance = float(input('Please, input here the total distance in km: '))
ticket_price = 0.5 * distance if distance <= 200 else 0.45 * distance

print(f'The ticket price is: R${ticket_price}')
