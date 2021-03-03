# Exercise 040: That classic of average
# Make a program that read two scores of a student and calculate your average
# Show a final message, according to the average reached.
# - Average lower than 5.0: reproved
# - Average between 5.0 and 6.9: recovery
# - Average higher than 7.0: approved

score1 = float(input('Input here the first score: '))
score2 = float(input('Input here the second score: '))
average = (score1 + score2) / 2

if average < 5:
    print(f'Your average is {average} - Reproved!')
elif 5 >= average < 7:
    print(f'Your average is {average} - Recovery!')
else:
    print(f'Your average is {average} - Approved!')
