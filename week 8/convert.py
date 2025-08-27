def repToDecimal(number, base):
    # Define a dictionary to store the values of digits
    digit_values = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    decimal = 0
    power = 0

    # Convert each digit to uppercase and calculate decimal value
    for digit in reversed(number.upper()):
        decimal += digit_values[digit] * (base ** power)
        power += 1

    return decimal

def main():
    # Test the repToDecimal function
    print(repToDecimal("10", 8))  # Output: 8
    print(repToDecimal("10", 16))  # Output: 16

if __name__ == "__main__":
    main()
