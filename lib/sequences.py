#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = [0, 1]

    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    for i in range(2, length):
        next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_number)
    print(fibonacci_sequence)


print_fibonacci(20)
