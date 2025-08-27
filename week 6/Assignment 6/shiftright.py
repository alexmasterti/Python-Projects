def shift_right(bit_string):
    shifted_bs = bit_string[-1] + bit_string[:-1]
    return shifted_bs

bit_string = input("Enter the bit string: ")
shifted_string = shift_right(bit_string)
print("Shifted string to the right: " + shifted_string)
