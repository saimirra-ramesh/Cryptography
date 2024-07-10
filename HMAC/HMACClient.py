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
            num = ord(ch.lower()) - ord('a')
            bits.append(str(bin(num))[2:].zfill(length))
    return bits


def hash_func(to_hash):
    to_hash = [to_hash[i:i+4] for i in range(0, len(to_hash), 4)]
    result = to_hash[0]

    for group in to_hash[1:]:
        result = xor(result, group)

    return result


def HMAC(message, k):
    b = 32

    # Message size: 32-bits - 8 alphabets [each represented as 4-bits]
    # message = input("Enter the Message: ").lower()

    k_plus = "".join(str_to_bits(k, 5)).zfill(b)
    message = "".join(str_to_bits(message, 4)).zfill(b)
    

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


# RSA Encryption
def encrypt(m, e, n):
    # C = M ^ e mod n
    encrypted_text = 1
    while e > 0:
        encrypted_text *= m
        encrypted_text %= n
        e -= 1
    return chr(encrypted_text)


HOST = "127.0.0.1"
PORT = 8080
r = socket.socket()

r.connect((HOST, PORT))
print("Message from Receiver: ", r.recv(1024).decode())

print("")
print("Using RSA Algorithm for Confidentiality.")
print("")

p = input("Enter p value: ")
q = input("Enter q value: ")
r.send(p.encode())
r.send(q.encode())

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

# S sends its PU to R
r.send(str(e).encode())
    
# R's public key
pu = r.recv(1024).decode()
print("Received Public Key from R: ", pu)


message = input("Enter the Message: ")
k = "hello"

hmac_result = HMAC(message, k)
print("HMAC Result: ", hmac_result)

to_encrypt = list(map(ord, message+hmac_result))
encrypted_msg = ""
for m in to_encrypt:
    encrypted_msg += encrypt(m, int(pu), n)

r.send(encrypted_msg.encode())
print("Encrypted Message: ", encrypted_msg)

print("Hashed & Encrypted Message Sent!")

r.close()