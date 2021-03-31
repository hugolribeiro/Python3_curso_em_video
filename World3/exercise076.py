# Exercise 076: Price list with tuple
# Make a program that have a tuple with product names and its price.
# At the end, show the prices and organize the data in table form.

table =    ('Pencil', 1.75,
            'Eraser', 2,
            'Notebook', 15.9,
            'Pencil Case', 25,
            'Protractor', 4.20,
            'Compass', 9.99,
            'Backpack', 120.32,
            'Pens', 22.30,
            'Book', 34.90)

print('-' * 60)
print(f'{"Price List":^60}')
print('-' * 60)
for item in range(0, len(table), 2):
    print(f'Name: {table[item]:.<30}Price: {table[item+1]:>7.2f}')
