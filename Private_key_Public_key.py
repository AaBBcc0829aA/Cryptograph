import os
import hashlib
import ecdsa

# Generate a random private key
#private_key = os.urandom(32)
private_key = 0x6f0d600775290fc8c81272bfed85d3b4d8e38e31bb49586ef323b4771945b2fb
# Generate the public key using the private key
sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
public_key = sk.get_verifying_key().to_string()

# Derive Bitcoin address from public key
public_key_hash = hashlib.sha256(public_key).digest()
address = hashlib.new('ripemd160', public_key_hash).hexdigest()
print(f"Private Key: {private_key.hex()}")
print(f"Public Key: {public_key.hex()}")
print(f"Address: {address}")
