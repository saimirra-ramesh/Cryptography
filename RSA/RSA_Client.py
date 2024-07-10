import socket

def encrypt(m, e, n):
    m = m - ord('a')
    # C = M ^ e mod n
    encrypted_text = 1
    while e > 0:
        encrypted_text *= m
        encrypted_text %= n
        e -= 1
    return chr(encrypted_text + ord('a'))
 

def decrypt(ct, key, n):
    plain_text = ""
    for c in ct:
        c = ord(c) - ord('a')
        # M = C ^ d mod n
        decrypted = 1
        d = key
        while d > 0:
            decrypted *= c
            decrypted %= n
            d -= 1
        plain_text += chr(decrypted + ord('a'))
    return plain_text



# Making Socket Connections
s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))
print("Connection Message from Process B: ", s.recv(1024).decode())
print('')

# Inputting p and q values 
# Making them available to both Process A and Process B
p = input("Enter value of p (Prime Number): ")
q = input("Enter value of q (Prime Number): ")
s.send(p.encode())
s.send(q.encode())
print('')


# Computing n and phi
n = int(p) * int(q)
print("n = p * q : ", n )
phi = (int(p) - 1) * (int(q) - 1)
print("Phi: ", phi)
print('')


# Choosing Public Key  - 'e' value
e = input("Enter 'e'  value such that 1 < e < phi: ")  
print('')


# Finding Multiplicative Inverse d which is the Private Key
i = 0
while True:
    if (i * int(e)) % phi == 1:
        d = i
        break
    i += 1

# Sending Public Key of Process A to Process B
s.send(str(e).encode())
#print("Public Key of Process A sent to Process B.")
print('')


# Receiving Public Key of Process B
public_key_B = s.recv(1024).decode()
print("Public Key Received from Process B:", public_key_B)
print('')

# Sending Message to B
message = input("Enter Message to send to Process B: ")
message = list(map(ord, message))
print('')


# Character-wise Encryption
encrypted_message = ""
for m in message:
    encrypted_message += encrypt(m, int(public_key_B), n)
    

# Sending the Encrypted Message
s.send(encrypted_message.encode())
print('')


# Receiving Reply from Process B
reply = s.recv(1024).decode()
decrypted_reply = decrypt(reply, d, n)
    
print("Decrypted Reply received from Process B:", decrypted_reply)

s.close()

