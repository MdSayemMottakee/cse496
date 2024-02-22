import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]  # Define the alphabet for the Base16 encoding, using the first 16 lowercase letters

def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))  # Convert character to 8-bit binary representation
        enc += ALPHABET[int(binary[:4], 2)]  # Take first 4 bits and encode using Base16
        enc += ALPHABET[int(binary[4:], 2)]  # Take last 4 bits and encode using Base16
    return enc

def b16_decode(encoded):
    decoded = ""
    for i in range(0, len(encoded), 2):
        binary = "{:04b}{:04b}".format(ALPHABET.index(encoded[i]), ALPHABET.index(encoded[i+1]))  # Decode Base16 to binary
        decoded += chr(int(binary, 2))  # Convert binary to character
    return decoded

def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET  # Convert character to index in the alphabet
    t2 = ord(k) - LOWERCASE_OFFSET  # Convert key character to index in the alphabet
    return ALPHABET[(t1 + t2) % len(ALPHABET)]  # Apply Caesar cipher with key

flag = "redacted"
key = "k"
assert all([k in ALPHABET for k in key])  # Assert all characters in the key are in the defined alphabet
assert len(key) == 1  # Assert key length is 1

# Encoding the flag using Base16 and encrypting it using Caesar cipher
b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
    enc += shift(c, key[i % len(key)])  # Encrypt each character of the Base16 encoded flag with Caesar cipher using the key

enc=input()  # Taking input for the encrypted message

decrypted_b16 = ""

# Decrypting the encrypted message by trying all keys in the alphabet
for key in ALPHABET:
    decrypted_b16 = ""
    for i, c in enumerate(enc):
        decrypted_b16 += shift(c, key)  # Decrypt each character of the encrypted message with Caesar cipher using the current key
    decrypted_message = b16_decode(decrypted_b16)  # Decode the decrypted Base16 message
    print("Trying key:", key)
    print("Decrypted message:", decrypted_message)  # Print the decrypted message
