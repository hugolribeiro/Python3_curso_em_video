# Exercise 070: Products statistics
# Make a program that reads the name and the price of several products.
# The program must ask the user to continue. At the end, show:
# A) What is the total spend in the buy.
# B) How many products costs over than R$ 1000.
# C) What is the name of the cheapest product.

total = 0
over_thousand = 0
name_cheapest = ''
cheapest_price = 0
keep_going = True
count_product = 0
while True:
    product_name = input('Product name: ')
    product_price = float(input('Product price: '))
    count_product += 1
    if count_product == 1 or product_price < cheapest_price:
        cheapest_price = product_price
        name_cheapest = product_name
    if product_price > 1000:
        over_thousand += 1
    total += product_price
    keep_going = " "
    while keep_going not in "YN" :
        keep_going = input('Do you want to continue?\n'
                           '[Y] - Yes\n'
                           '[N] - No\n').strip().upper()
    if keep_going == 'N':
        print('Wrong choice, input again')
        break
print(f'A - Total spent: R$ {total:.2f}\n'
      f'B - {over_thousand} products over than R$ 1000\n'
      f'C - {name_cheapest} was the cheapest product. Its cost R$ {cheapest_price:.2f}')
