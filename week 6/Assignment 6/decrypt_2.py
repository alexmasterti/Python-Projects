def caesar_cipher_decrypt(text, distance):
    decrypted_text = ""
    for char in text:
        if char.isprintable():
            decrypted_char = chr((ord(char) - distance) % 256)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

file_path = input("Enter the path to the file to decrypt: ")
distance = int(input("Enter the distance value: "))

with open(file_path, 'r') as file:
    text = file.read()

decrypted_text = caesar_cipher_decrypt(text, distance)

with open(file_path, 'w') as file:
    file.write(decrypted_text)

print("File decrypted successfully.")

