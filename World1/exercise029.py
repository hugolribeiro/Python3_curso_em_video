# Exercise 029: traffic control radar
# Write a program that read the car's speed. If it exceeds 80 km/h, show a message if the driver has been fined.
# The fine will cost R$ 7,00 per each km that exceed 80km/h


car_speed = int(input('Input here the car\'s speed: '))
if car_speed > 80:
    print('Exceeded the speed limit. Fine applied.')
    fine = (car_speed - 80) * 7
    print(f'You need to pay a fine of the value R${fine}')
