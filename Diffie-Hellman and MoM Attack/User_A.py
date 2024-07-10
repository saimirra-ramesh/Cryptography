import socket
import diffie_hellman

# Predefined prime number (p) and its primitive root (g)
prime = 17
primitive_root = 3
HOST = "127.0.0.1"
PORT = 8080

# Connect to the server
s = socket.socket()
s.connect((HOST, PORT))

# Generate User A's private key
private_key = diffie_hellman.generate_private_key(prime, primitive_root)

# Generate User A's public key
public_key = diffie_hellman.generate_public_key(prime, primitive_root, private_key)

# Send User A's public key to the server
s.send(str(public_key).encode())
print("Public Key Sent: ", public_key)

# Receive the server's public key
received_public_key = int(s.recv(1024).decode())
print("Public Key Received: ", received_public_key)

# Calculate the final shared key
shared_key = diffie_hellman.calculate_shared_key(received_public_key, private_key, prime)
print("Final Key: ", shared_key)

# Close the connection
s.close()
