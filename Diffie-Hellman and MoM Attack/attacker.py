import socket
import diffie_hellman
import threading

# Defining prime number (p) and its primitive root (a)
prime = 17  #17
a = 3
HOST = '127.0.0.1'

# User A will connect to this port
A = 8080  

# User B listens to this port
# Attacker redirects User A to this port
B = 8081   

def handle_user_a():
    #Handle User A
    with socket.socket() as listener_a:
        listener_a.bind((HOST, A))
        listener_a.listen(5)
        print(f"Attacker listening for User A on port {A}")
        
        conn_a, _ = listener_a.accept()
        with conn_a:
            print('')
            print(f"Connection from User A accepted")
            print('')
            # Generate attacker's private and public keys for User A
            private_key_a = diffie_hellman.generate_private_key(prime, a)
            public_key_a = diffie_hellman.generate_public_key(prime, a, private_key_a)
            

            # Receive public key from User A
            received_public_key_a = int(conn_a.recv(1024).decode())
            print(f"Public Key from User A: {received_public_key_a}")
            

            # Send attacker's public key to User A, pretending it's from User B
            conn_a.send(str(public_key_a).encode())
            print(f"Public Key sent to User A: {public_key_a}")
            

            # Calculate the key with User A
            shared_key_a = diffie_hellman.calculate_shared_key(received_public_key_a, private_key_a, prime)
            print(f"Calculated Key with User A: {shared_key_a}")
            

def handle_user_b():
    #Handle User B
    with socket.socket() as s_b:
        s_b.connect((HOST, B))  # Connect to User B as User A
        print("Connected with User B")
        # Generate attacker's private and public keys for User B
        private_key_b = diffie_hellman.generate_private_key(prime, a)
        public_key_b = diffie_hellman.generate_public_key(prime, a, private_key_b)
        

        # Send attacker's public key to User B, pretending it's from User A
        s_b.send(str(public_key_b).encode())
        print(f"Public Key sent to User B: {public_key_b}")
        

        # Receive public key from User B
        received_public_key_b = int(s_b.recv(1024).decode())
        print(f"Public Key from User B: {received_public_key_b}")
        

        # Calculate the key with User B
        shared_key_b = diffie_hellman.calculate_shared_key(received_public_key_b, private_key_b, prime)
        print(f"Calculated Key with User B: {shared_key_b}")
        

thread_a = threading.Thread(target=handle_user_a)
thread_b = threading.Thread(target=handle_user_b)
thread_a.start()
thread_b.start()
thread_a.join()
thread_b.join()
