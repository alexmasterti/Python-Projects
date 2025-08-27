def shift_right(bit_string):
    shifted_string = bit_string[-1] + bit_string[:-1]
    print("Shifted right:", shifted_string)

def main():
    bit_string = input("Enter a bit string: ")
    shift_right(bit_string)

if __name__ == "__main__":
    main()
