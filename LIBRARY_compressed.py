from ecdsa import SigningKey, SECP256k1

def get_public_keys(private_hex):
    # Convert hex private key to bytes
    private_bytes = bytes.fromhex(private_hex)
    # Generate public key
    sk = SigningKey.from_string(private_bytes, curve=SECP256k1)
    vk = sk.verifying_key  # Public key object
    # Get x and y coordinates
    x, y = vk.pubkey.point.x(), vk.pubkey.point.y()

    print(f"x: {x:064X}")
    print(f"y: {y:064X}")
    
    # Uncompressed public key (04 + x + y)
    uncompressed_pubkey = f"04{x:064X}{y:064X}"
    # Compressed public key
    prefix = "02" if y % 2 == 0 else "03"
    compressed_pubkey = f"{prefix}{x:064X}"
    return uncompressed_pubkey, compressed_pubkey

# Example Usage
private_key_hex = "1E99423A4ED27608A15A2616F81652DCDD9F69D398B5C3F1F3567E24D10B2C77"
uncompressed, compressed = get_public_keys(private_key_hex)
print("Uncompressed Public Key:", uncompressed)
print("Compressed Public Key:  ", compressed)
