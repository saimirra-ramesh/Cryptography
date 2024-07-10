# Verifies the signature; Print v

# H(M) must not be 0
def hash(input_num: str):
    hash_val = 1
    for digit in input_num:
        if digit.isalpha():
            digit = digit.upper()
            digit = 10 + ord('A') - ord(digit)
        hash_val ^= int(digit)
    return hash_val % 10

def mul_inverse(k, q) :
    for i in range(1, q):
        if (k * i) % q == 1:
            return i

import socket

HOST = "127.0.0.1"
PORT = 8080

receiver = socket.socket()
receiver.bind((HOST, PORT))

receiver.listen(5)
print("")
print("")
print("Socket is listening...")

while True:
    sck, addr = receiver.accept()
    print("Connection from ", addr, " accepted")
    sck.send("Thank you for connecting".encode())

    p = int(sck.recv(1024).decode())
    sck.send("Received p".encode())
    q = int(sck.recv(1024).decode())
    sck.send("Received q".encode())
    y = int(sck.recv(1024).decode())
    sck.send("Received y".encode())
    g = int(sck.recv(1024).decode())
    sck.send("Received g".encode())
    
    M = sck.recv(1024).decode()
    sck.send("Received M".encode())
    r = int(sck.recv(1024).decode())
    sck.send("Received r".encode())
    s = int(sck.recv(1024).decode())
    sck.send("Received s".encode())

    # Verifying
    w = mul_inverse(s, q)
    u1 = int(hash(M) * w) % q
    u2 = int(r*w) % q
    v = (int((g ** u1) * (y ** u2)) % p) % q
    print("v calculated: ", v)
    print("Valid: ", v == r)

    receiver.close()
    break
