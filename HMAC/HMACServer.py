import socket

def xor(num1, num2):
    result = ""
    for i, digit in enumerate(num1):
        if num2[i] == digit:
            result += "0"
        else:
            result += "1"
    return result

def str_to_bits(string, length):
    bits = []
    for ch in string:
        if ch.isalpha():
            num = ord(ch.upper()) - ord('A')
            bits.append(str(bin(num))[2:].zfill(length))
    return bits

def hash_func(to_hash):
    to_hash = [to_hash[i:i+4] for i in range(0, len(to_hash), 4)]
    result = to_hash[0]
    # print(to_hash)

    for group in to_hash[1:]:
        result = xor(result, group)
    # print(result)
    return result

def HMAC(message, k):
    b = 32

    # Message size: 32-bits - 8 alphabets [each represented as 4-bits]
    # message = input("Enter the Message: ").lower()
    # k = input("Enter the Secret Key: ").lower()

    k_plus = "".join(str_to_bits(k, 5)).zfill(b)
    message = "".join(str_to_bits(message, 4)).zfill(b)
    # print(message, k_plus)

    ipad = "00110110" * (b // 8) # 0x36
    opad = "01011100" * (b // 8) # 0x5C

    Si = xor(ipad, k_plus)
    S0 = xor(opad, k_plus)

    to_hash = Si + message
    H = hash_func(to_hash)

    to_hash = S0 + H
    HMAC_result = hash_func(to_hash)
    print(HMAC_result)
    return HMAC_result

#RSA Decryption
def decrypt(ct, key, n):
    plain_text = ""
    for c in ct:
        c = ord(c)
        # M = C ^ d mod n
        decrypted = (c ** key) % n
        plain_text += chr(decrypted)
    return plain_text


HOST = "127.0.0.1"
PORT = 8080

r = socket.socket()
r.bind((HOST, PORT))
r.listen(5)
print("")
print("Socket is listening...")

# Connecting with the sender
while True:
    s, addr = r.accept()
    print("Connection from ", addr, " accepted.")
    s.send("Thank you for connecting.".encode())
    print("")

    p = s.recv(1024).decode()
    q = s.recv(1024).decode()
    print("Received p from Sender: ", p)
    print("Received q from Sender: ", q)

    # S's public key
    pu = s.recv(1024).decode()
    print("Received Public Key from S: ", pu)

    n = int(p) * int(q)
    phi = (int(p) - 1) * (int(q) - 1)
    print("phi = ", phi)
    # Public Key: (e, n)
    e = input("Choose value of e such that (1 < e < phi): ") 
    print("")

    i = 0
    while True:
        if (i * int(e)) % phi == 1:
            # Private Key: (d, n)
            d = i 
            break
        i += 1


    # R sends its Public Key to S
    s.send(str(e).encode())

    received_text = s.recv(1024).decode()
    print("Text Received: ", received_text)
    print("")

    received_message, received_hmac = decrypt(received_text, d, n)[:8], decrypt(received_text, d, n)[8:]


    print("After Decryption: ")
    print("Message: ", received_message)
    print("HMAC received: ", received_hmac)

    print("")
    print("Verifying Authenticity: ")

    # Verifying Authentication
    k = "hello"
    hmac_result = HMAC(received_message, k)

    print("Message is authentic: ", hmac_result == received_hmac)

    r.close()
    break