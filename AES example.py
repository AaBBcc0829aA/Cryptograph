from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# Key and IV (Initialization Vector)
key = b"thisisasecretkey"  # 16 bytes for AES-128
iv = b"thisisanivector1"  # 16 bytes IV

# Input plaintext
plaintext = b"Hello, AES encryption!"

# Pad plaintext to be a multiple of 16 bytes
padder = padding.PKCS7(128).padder()
padded_plaintext = padder.update(plaintext) + padder.finalize()

# Encrypt
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

print("Ciphertext:", ciphertext)

# Decrypt
decryptor = cipher.decryptor()
decrypted_padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

# Remove padding
unpadder = padding.PKCS7(128).unpadder()
decrypted_plaintext = unpadder.update(decrypted_padded_plaintext) + unpadder.finalize()

print("Decrypted plaintext:", decrypted_plaintext)
