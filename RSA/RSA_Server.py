import socket

s = socket.socket()
print("Connection Established Successsfully!")

port = 12345
s.bind(('127.0.0.1', port))

s.listen(5)
print("Socket is Listening...")


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

 
while True:

    print('')

    # Making Socket Connections
    c, addr = s.accept()
    print("Got Connection from", addr)
    c.send("Thank you for Connecting!".encode())
    print('')


    # Receiving values of p and q chosen by user 
    p = c.recv(1024).decode()
    q = c.recv(1024).decode()
    print("Received p from Process A: ", p)
    print("Received q from Process A: ", q)


    # Computing n and phi
    n = int(p) * int(q)
    print("n = p * q : ", n )
    phi = (int(p) - 1) * (int(q) - 1)
    print("Phi: ", phi)
    print('')


    # Receiving Public Key of Process A
    public_key_A = c.recv(1024).decode()
    print("Public Key Received from Process A: ", public_key_A)
    print('')


    # Choosing Public Key  - 'e' value
    e = input("Enter 'e'  value such that 1 < e < phi : ")
    print('')

    # Sending Public Key of Process B to Process A
    c.send(str(e).encode())


    # Finding Multiplicative Inverse d which is the Private Key
    i = 0
    while True:
        if (i * int(e)) % phi == 1:
            d = i # Private Key => (n, d)
            break
        i += 1

    # Receiving Message from A
    message = c.recv(1024).decode()
    message = decrypt(message, d, n)
    print("Message received from Process A: ", message)
    print('')
    

    # Sending Reply to Process A
    reply = input("Enter Reply to send to Process A: ")
    reply = list(map(ord, reply))

    encrypted_msg = ""
    for m in reply:
        encrypted_msg += encrypt(m, int(public_key_A), n)
    c.send(encrypted_msg.encode())

    c.close()
    break
