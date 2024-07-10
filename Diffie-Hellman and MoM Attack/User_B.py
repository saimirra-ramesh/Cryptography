import socket
import diffie_hellman

# Predefined prime number (p) and its primitive root (g)
prime = 17
primitive_root = 3
HOST = "127.0.0.1"
PORT = 8081

# Create a socket object
r = socket.socket()

# Bind the socket to the host and port
r.bind((HOST, PORT))

# Listen for incoming connections
r.listen(5)
print('')
print("Socket is listening...")

while True:
    # Accept incoming connection
    s, addr = r.accept()
    print("Connection from User A at", addr, " accepted")

    # Generate User B's private key
    private_key = diffie_hellman.generate_private_key(prime, primitive_root)

    # Generate User B's public key
    public_key = diffie_hellman.generate_public_key(prime, primitive_root, private_key)

    # Receive User A's public key
    received_public_key = int(s.recv(1024).decode())
    print("Public Key Received: ", received_public_key)

    # Send User B's public key to User A
    s.send(str(public_key).encode())
    print("Public Key Sent: ", public_key)

    # Calculate the final shared key
    shared_key = diffie_hellman.calculate_shared_key(received_public_key, private_key, prime)
    print("Final Key: ", shared_key)

    # Close the connection
    s.close()
    break  # Break out of the loop after handling one connection
