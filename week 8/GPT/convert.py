def repToDecimal(string, base):
    lookup_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    'A': 10, 'B': 11, 'C': 12, 'D': 13,
                    'E': 14, 'F': 15}

    decimal = 0
    power = len(string) - 1
    for digit in string:
        decimal += lookup_table[digit.upper()] * (base ** power)
        power -= 1
    return decimal


def main():
    test_cases = [("10", 8), ("10", 16), ("1010", 2), ("FF", 16)]
    for number, base in test_cases:
        print(f"Base {base} representation of {number}:", repToDecimal(number, base))


if __name__ == "__main__":
    main() 
