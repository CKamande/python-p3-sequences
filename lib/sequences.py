#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []

    if length == 0:
        print(sequence)  # This ensures []\n is printed when length = 0
        return

    sequence.append(0)

    if length == 1:
        print(sequence)
        return

    sequence.append(1)

    for _ in range(2, length):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)

    print(sequence)

