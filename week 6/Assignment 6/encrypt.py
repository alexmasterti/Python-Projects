def caesar_cipher_encrypt(text, distance):
    encrypted_text = ""
    for char in text:
        if char.isprintable():
            encrypted_char = chr((ord(char) + distance) % 256)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

plaintext = input("Enter the plaintext: ")
distance = int(input("Enter the distance value: "))
encrypted_text = caesar_cipher_encrypt(plaintext, distance)
print("Encrypted text: " + encrypted_text)
