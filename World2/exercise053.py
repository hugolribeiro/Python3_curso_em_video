# Palindrome detector
# Make a program that read any phrase and tell if it is a palindrome, not considering the spaces.

phrase = input('Phrase: ').replace(' ', '').lower()
reverse_phrase = phrase[::-1]
if phrase == reverse_phrase:
    print(f'Phrase: {phrase}\n'
          f'Reverse phrase: {reverse_phrase}\n'
          f'We have a palindrome here!')
else:
    print(f'Phrase: {phrase}\n'
          f'Reverse phrase: {reverse_phrase}\n'
          f'It ins\'t a palindrome.')
