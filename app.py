def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha()
            shift = ord(key[key_index]) - ord('A')
            new_char = chr((ord(char) + shift) % 26 + ord('A'))
            encrypted_text += new_char
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char
    return encrypted_text

plaintext = input("Enter plaintext: ")
key = input("Enter key: ")
ciphertext = vigenere_encrypt(plaintext, key)
print("Encrypted Text:", ciphertext)