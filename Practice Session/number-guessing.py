# Codejam 2018, Practice Session: Number Guessing

import sys

# I/O Code - Simple Binary Search
num_cases = int(input())

for case in range(num_cases):
    A, B = [int(i) + 1 for i in input().split()]
    num_guesses = int(input())
    guess = (A + B)//2
    for _ in range(num_guesses):
        print(guess, flush=True)
        message = input()
        if message == 'CORRECT':
            break
        elif message == 'TOO_SMALL':
            A = guess
            guess = (A + B)//2
        elif message == 'TOO_BIG':
            B = guess
            guess = (A + B)//2
        else:
            sys.exit()

sys.exit()