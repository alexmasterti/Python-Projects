def decimal_to_rep(decimal, base):
    digits = "0123456789ABCDEF"
    if decimal == 0:
        return "0"
    representation = ""
    while decimal > 0:
        remainder = decimal % base
        representation = digits[remainder] + representation
        decimal //= base
    return representation

def main():
    test_cases = [(8, 8), (16, 16), (10, 2), (123, 5)]
    for decimal, base in test_cases:
        print(f"{decimal} in decimal is {decimal_to_rep(decimal, base)} in base {base}.")

if __name__ == "__main__":
    main()
