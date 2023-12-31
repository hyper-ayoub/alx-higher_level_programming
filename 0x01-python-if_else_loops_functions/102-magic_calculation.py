#!/usr/bin/python3

def magic_calculation(a, b, c):
    if a < b:
        return c

    if c > b:
        return a + b
    else:
        return a * b - c


if __name__ == "__main__":
    # Test cases
    print(magic_calculation(3, 5, 7))
    print(magic_calculation(8, 6, 10))
    print(magic_calculation(5, 3, 1))
