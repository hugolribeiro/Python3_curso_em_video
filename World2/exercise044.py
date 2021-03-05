# Exercise 044: Payments management
# Make a program that calculate the value to be paid of a product.
# According its regular price, and the payment condition:
# - In cash or check: 10% of discount
# - In cash using the card: 5% of discount
# - 2 times in card: regular price
# - 3 times or more in card: 20% of juros

regular_price = float(input('Input here the product regular price: '))
payment_condition = int(input('Payment Condition\n'
                              '[1] - In cash (money or check)\n'
                              '[2] - In cash (card)\n'
                              '[3] - 2 times in card\n'
                              '[4] - 3 or more times in card\n'))

if payment_condition == 1:
    total = regular_price * 0.9
elif payment_condition == 2:
    total = regular_price * .95
elif payment_condition == 3:
    total = regular_price
    quota = total / 2
    print(f'Your purchase will be divided in 2x of R$ {quota} without juros ')
elif payment_condition == 4:
    total = regular_price * 1.2
    amount_quotes = int(input('How many quotes? '))
    quote = total / amount_quotes
    print(f'Your purchase will be divided in {amount_quotes} times of R$ {quote} with juros')
else:
    total = regular_price
    print('Invalid option. Try again!')
print(f'your purchase of R$ {regular_price} will cost R$ {total} at the final')
