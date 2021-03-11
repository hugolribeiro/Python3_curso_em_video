# Exercise 063: Fibonacci Sequence v1.0
# Write a program that read an any 'n' integer number and show the 'n' firsts elements of a Fibonacci Sequence.
# Example: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

fibonacci_sequence = [0, 1]
n_elements = int(input('How many terms do you want see? '))

for term in range(2, n_elements):
    fibonacci_sequence.append(fibonacci_sequence[term-1] + fibonacci_sequence[term-2])
print(' -> '.join(list(map(str, fibonacci_sequence[:n_elements]))), end=' END ')
