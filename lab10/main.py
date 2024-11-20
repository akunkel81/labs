from string import ascii_lowercase as lowercase


def shift_char(char, key):
    base = ord('a')
    shifted = (ord(char.lower()) - base + key) % 26 + base
    return chr(shifted)

def shift_special(char, key):
    return chr((ord(char) + key) % 128)

def encrypt(plaintext, key):
    return ''.join(
        shift_char(char, key) if char.isalpha() else
        shift_special(char, key) if not char.isspace() else char
        for char in plaintext
    )

def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)


key = 3
encrypted = encrypt("hello WORLD!", key)
print("Encrypted:", encrypted)  # Output: "KHOOR zruog$"

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)  # Output: "hello WORLD!"



