# Exercise 020: First and Last ocurrence in a String.
# Make a program that read a phrase and show:
# How many times appears the letter "A".
# In which position it appears at the first time
# In which position it appears at the last time.

phrase = input('Input here a phrase: ')
times = (phrase.upper()).count('A')
first_position = phrase.upper().find('A')+1
last_position = phrase.upper().rfind('A')+1

print(f'Times: {times}\n'
      f'First position: {first_position}\n'
      f'Last position: {last_position}')