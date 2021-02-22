# Exercise 024: Verifying the firsts letters in a text
# Make a program that read the name of a city and tell if it start ou no with the name "SANTO".

city_name = input('Input here a city name: ')
if (city_name.upper()).startswith("SANTO"):
    print(f'Yes! The city {city_name} starts with "SANTO"')
else:
    print(f'No! The city {city_name} doens\'t start with "SANTO"')
