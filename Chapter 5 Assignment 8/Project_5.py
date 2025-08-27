def rep_to_decimal(number, base):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'A': 10, 'B': 11, 'C': 12, 'D': 13,
              'E': 14, 'F': 15}

    decimal = 0
    power = 0
    for digit in reversed(number):
        decimal += digits[digit.upper()] * (base ** power)
        power += 1
    return decimal

def main():
    test_cases = [("10", 8), ("10", 16), ("1010", 2), ("123", 5)]
    for number, base in test_cases:
        print(f"{number} in base {base} is {rep_to_decimal(number, base)} in decimal.")

if __name__ == "__main__":
    main()
