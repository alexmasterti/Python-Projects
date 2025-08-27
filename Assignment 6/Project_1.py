def encrypt_char(char, distance):
    if char.isprintable():
        encrypted_char = chr((ord(char) - 32 + distance) % 94 + 32)
        return encrypted_char
    else:
        return char

def caesar_cipher(plaintext, distance):
    encrypted_text = ""
    for char in plaintext:
        encrypted_text += encrypt_char(char, distance)
    return encrypted_text

def get_input():
    plaintext = input("Enter a line of plaintext: ")
    distance = int(input("Enter the distance value: "))
    return plaintext, distance

def main():
    plaintext, distance = get_input()
    encrypted_text = caesar_cipher(plaintext, distance)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
