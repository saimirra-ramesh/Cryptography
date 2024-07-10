import random

# Function to generate private key
def generate_private_key(prime, primitive_root):
    return random.randint(1, prime)

# Function to generate public key
def generate_public_key(prime, primitive_root, private_key):
    return (primitive_root ** private_key) % prime

# Function to calculate the shared key
def calculate_shared_key(received_public_key, private_key, prime):
    return (received_public_key ** private_key) % prime

