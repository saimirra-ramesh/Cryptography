import socket
import random

def hash(input_num: str):
    hash_val = 1
    for digit in input_num:
        if digit.isalpha():
            digit = digit.upper()
            digit = 10 + ord('A') - ord(digit)
        hash_val ^= int(digit)
    return hash_val % 10

def find_g(p, q):
    d = (p - 1) / q
    h = random.randrange(1, p-1)
    while (h ** d) % p <= 1:
        h = random.randrange(1, p-1)
    g = (h ** d) % p
    return g

def mul_inverse(k, q) :
    for i in range(1, q):
        if (k * i) % q == 1:
            return i
    return i


#Making Connections to the Server
HOST = "127.0.0.1"
PORT = 8080

sck = socket.socket()
sck.connect((HOST, PORT))
print("")
print("")
print("Message from Receiver: ", sck.recv(1024).decode())

p = int(input("Enter p: "))
q = int(input("Enter q: "))
M = input("Enter Message: ")

g = int(find_g(p, q))

# User's Private Key
x = 5   #random.randint(0, q)

# User's Public Key
y = int(g ** x) % p
k = 3   #random.randint(0, q)


# Signing
r = int((g ** k) % p) % q
s = int(mul_inverse(k, q) * (hash(M) + x*r)) % q

#To be sent to Server
print("Signature: ", (M, r, s))

p, q, y, g = str(p), str(q), str(y), str(g)
sck.send(p.encode())
print("Message from Receiver: ", sck.recv(1024).decode())
sck.send(q.encode())
print("Message from Receiver: ", sck.recv(1024).decode())
sck.send(y.encode())
print("Message from Receiver: ", sck.recv(1024).decode())
sck.send(g.encode())
print("Message from Receiver: ", sck.recv(1024).decode())

r, s = str(r), str(s)
sck.send(M.encode())
print("Message from Receiver: ", sck.recv(1024).decode())
sck.send(r.encode())
print("Message from Receiver: ", sck.recv(1024).decode())
sck.send(s.encode())
print("Message from Receiver: ", sck.recv(1024).decode())

sck.close()