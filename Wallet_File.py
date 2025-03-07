from cryptography.fernet import Fernet

private_key=0x6f0d600775290fc8c81272bfed85d3b4d8e38e31bb49586ef323b4771945b2fb

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt the private key
encrypted_private_key = cipher_suite.encrypt(private_key)

# Save the encrypted key to a file
with open('wallet.dat', 'wb') as f:
    f.write(encrypted_private_key)
