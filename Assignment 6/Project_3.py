def encrypt_char(char, distance):
    if char.isprintable():
        encrypted_char = chr((ord(char) - 32 + distance) % 94 + 32)
        return encrypted_char
    else:
        return char

def caesar_encrypt(plaintext, distance):
    encrypted_text = ""
    for char in plaintext:
        encrypted_text += encrypt_char(char, distance)
    return encrypted_text

def encrypt_file(input_file, output_file, distance):
    with open(input_file, 'r') as file:
        plaintext = file.read()
    encrypted_text = caesar_encrypt(plaintext, distance)
    with open(output_file, 'w') as file:
        file.write(encrypted_text)

def decrypt_char(char, distance):
    if char.isprintable():
        decrypted_char = chr((ord(char) - 32 - distance) % 94 + 32)
        return decrypted_char
    else:
        return char

def caesar_decrypt(encrypted_text, distance):
    plaintext = ""
    for char in encrypted_text:
        plaintext += decrypt_char(char, distance)
    return plaintext

def decrypt_file(input_file, output_file, distance):
    with open(input_file, 'r') as file:
        encrypted_text = file.read()
    plaintext = caesar_decrypt(encrypted_text, distance)
    with open(output_file, 'w') as file:
        file.write(plaintext)

def main():
    mode = input("Choose mode (encrypt/decrypt): ").lower()
    if mode == "encrypt":
        input_file = input("Enter the name of the input file: ")
        output_file = input("Enter the name of the output file: ")
        distance = int(input("Enter the distance value: "))
        encrypt_file(input_file, output_file, distance)
        print("Encryption complete.")
    elif mode == "decrypt":
        input_file = input("Enter the name of the input file: ")
        output_file = input("Enter the name of the output file: ")
        distance = int(input("Enter the distance value: "))
        decrypt_file(input_file, output_file, distance)
        print("Decryption complete.")
    else:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
