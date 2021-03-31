# Exercise 077: Counting vowels in a tuple
# Make a program that have a tuple with several words
# After that, you have to show, for each word, which are its vowels.

words = ('fly', 'walk', 'ladder', 'notebook', 'bird', 'whale',
         'dig', 'cavern', 'sky', 'ocean', 'sand', 'thousands')

for word in words:
    print(f'{word} = ', end='')
    for letter in word:
        if letter in ('aeiou'):
            print(letter, end='')
    print()
