def caesar_cipher_encrypt(text, distance):
    encrypted_text = ""
    for char in text:
        if char.isprintable():
            encrypted_char = chr((ord(char) + distance) % 256)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

file_path = input("Enter the path to the file to encrypt: ")
distance = int(input("Enter the distance value: "))

with open(file_path, 'r') as file:
    text = file.read()

encrypted_text = caesar_cipher_encrypt(text, distance)

with open(file_path, 'w') as file:
    file.write(encrypted_text)

print("File encrypted successfully.")

