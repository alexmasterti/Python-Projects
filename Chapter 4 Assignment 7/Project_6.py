def char_to_binary(char):
    binary_value = bin(ord(char) + 1)[2:]
    return binary_value.zfill(8)

def encrypt(text):
    encrypted_text = ""
    for char in text:
        binary_value = char_to_binary(char)
        shifted_binary = binary_value[1:] + binary_value[0]
        encrypted_text += shifted_binary + " "
    return encrypted_text.strip()

def main():
    plaintext = input("Enter the text to encrypt: ")
    encrypted_text = encrypt(plaintext)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
