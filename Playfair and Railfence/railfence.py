# Rail Fence Method

print('---------------------------------------------')
plain_text = input("Plain Text: ")
depth = int(input("Depth: ")) # No of rows
print('---------------------------------------------')

plain_text = plain_text.upper()

table = [list(plain_text[i:i+depth]) for i in range(0, len(plain_text), depth)]
while len(table[-1]) != len(table[0]):
    table[-1].append(' ')

# Transposing the table
table = list(zip(*table))

print("Matrix")
for row in table:
    print('  '.join(row))
print('---------------------------------------------')

cipher_text = ''
for row in table:
    cipher_text += ''.join(row).strip()

cipher_text = cipher_text

print('Cipher Text: ', cipher_text)
print('---------------------------------------------')