def decrypt_char(char, distance):
    if char.isprintable():
        decrypted_char = chr((ord(char) - 32 - distance) % 94 + 32)
        return decrypted_char
    else:
        return char

def caesar_decipher(encrypted_text, distance):
    plaintext = ""
    for char in encrypted_text:
        plaintext += decrypt_char(char, distance)
    return plaintext

def get_input():
    encrypted_text = input("Enter a line of encrypted text: ")
    distance = int(input("Enter the distance value: "))
    return encrypted_text, distance

def main():
    encrypted_text, distance = get_input()
    plaintext = caesar_decipher(encrypted_text, distance)
    print("Decrypted text:", plaintext)

if __name__ == "__main__":
    main()
