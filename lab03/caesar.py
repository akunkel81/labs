class Caesar:
    def __init__(self, key=0):
        self._key = key

    def get_key(self):
        return self._key

    def set_key(self, key):
        self._key = key

    def encrypt(self, plaintext):
        ciphertext = []
        for char in plaintext:
            if char.isalpha():
                shifted = self.shift_char(char, self._key)
                ciphertext.append(shifted)
            elif not char.isspace():
                ciphertext.append(self.shift_special(char, self._key))
            else:
                ciphertext.append(char)
        return ''.join(ciphertext)

    def decrypt(self, ciphertext):
        plaintext = []
        for char in ciphertext:
            if char.isalpha():
                shifted = self.shift_char(char, -self._key)
                plaintext.append(shifted)
            elif not char.isspace():
                plaintext.append(self.shift_special(char, -self._key))
            else:
                plaintext.append(char)
        return ''.join(plaintext)

    def shift_char(self, char, key):
        char = char.lower()
        base = ord('a')
        shifted = (ord(char) - base + key) % 26 + base
        return chr(shifted)


    def shift_special(self, char, key):
        return chr((ord(char) + key) % 128)


cipher = Caesar()

cipher.set_key(3)
print(cipher.encrypt("hello WORLD!"))

print(cipher.decrypt("KHOOR zruog$"))

cipher.set_key(6)
print(cipher.encrypt("zzz"))
print(cipher.decrypt("FFF"))

cipher.set_key(-6)
print(cipher.encrypt("FFF"))
