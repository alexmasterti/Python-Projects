def shift_left(bit_string):
    shifted_string = bit_string[1:] + bit_string[0]
    print("Shifted left:", shifted_string)

def main():
    bit_string = input("Enter a bit string: ")
    shift_left(bit_string)

if __name__ == "__main__":
    main()
