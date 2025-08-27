def shift_left(bit_string):
    shifted_bs = bit_string[1:] + bit_string[0]
    return shifted_bs

bit_string = input("Enter the bit string: ")
shifted_string = shift_left(bit_string)
print("Shifted string to the left: " + shifted_string)
