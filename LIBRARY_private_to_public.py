import ecdsa
import binascii

def private_to_public(private_key_hex):
    # Convert hex private key to bytes
    private_key_bytes = bytes.fromhex(private_key_hex)
    # Create private key object
    sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    # Get public key object
    vk = sk.verifying_key
    # Convert to uncompressed public key format (04 + X + Y)
    public_key_bytes = b"\x04" + vk.to_string()
    # Return as hex
    return binascii.hexlify(public_key_bytes).decode()

# Example usage
private_key_hex = "1E99423A4ED27608A15A2616EE3FCF5B453D1D5F47624C4A3B25E84B669F59C7" # Replace with your private key
print("Private_key:", private_key_hex)
public_key = private_to_public(private_key_hex)
print("Public Key:", public_key)
