# Exercise 043: body mass index (BMI)
# Make a program that read the weight and the height of a person.
# Calculate his BMI and show your status, according with the table below:
# - Up to 18.5 (not include): Under weight
# - Between 18.5 and 25: Ideal weight
# - Between 25 and 30: Overweight
# - Between 30 and 40: Obesity
# - Above than 40: Morbid obesity

# Formula: BMI = kg / m²

weight = float(input('Input here the weight in kg: '))
height = float(input('Input here the height in meter: '))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print('Under weight')
elif 18.5 <= bmi < 25:
    print('Ideal weight')
elif 25 <= bmi < 30:
    print('Overweight')
elif 30 <= bmi < 40:
    print('Obesity')
else:
    print('Morbid obesity')
