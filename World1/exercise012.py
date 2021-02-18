# Exercise 012: Calculating discounts
# Make an algorithm that read the price of a product and show its new price, with 5% of discount

price = float(input('Input here the product price: '))
discount = 5
new_price = price * (100 - discount)/100

print(f'The new price is: {new_price}')
