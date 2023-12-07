# lib/sequences.py

def print_fibonacci(length):
    if length <= 0:
        return []

    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print(fibonacci_sequence[:length])

