# Playfair Cipher
 
def split(text):
    pairs = pairup(text)
    for i, pair in enumerate(pairs):
        if len(pair) == 2 and len(set(pair)) == 1:
            text.insert(i * 2 + 1, 'x')
            pairs = split(text)
            break
    if len(pairs[-1]) == 1:
        pairs[-1].append('x')
    return pairs
 
def pairup(text):
    return [text[i:i+2] for i in range(0, len(text), 2)]
 
print('---------------------------------------------')
plain_text = input("Plain Text: ")
keyword = input("Keyword: ")
print('---------------------------------------------')
  
plain_text = list(plain_text)
keyword = list(keyword)
used = []
alphabets = [chr(i) for i in range(97, 123) if chr(i) != 'j']
key = []
 
for letter in keyword:
    if letter not in used:
        key.append(letter.upper())
        used.append(letter)
        alphabets.remove(letter)
 
for i in range(26 - len(used) - 1):    
    letter = alphabets.pop(0)
    key.append(letter.upper())
 
table = [key[i:i+5] for i in [0, 5, 10, 15, 20]]

print("5x5 Matrix")
for row in table:
    print('  '.join(row))
print('---------------------------------------------')

cipher_text = []

for l1, l2 in split(plain_text):
    if l1 == 'j': l1 = 'i'
    if l2 == 'j': l2 = 'i'

    for i, row in enumerate(table):
        if l1.upper() in row:
            coords1 = (i, row.index(l1.upper()))
        if l2.upper() in row:
            coords2 = (i, row.index(l2.upper()))
    
    # Same row
    if coords1[0] == coords2[0]:
        cipher_text.append(table[coords1[0]][(coords1[1] + 1) % 5])
        cipher_text.append(table[coords2[0]][(coords2[1] + 1) % 5])

    # Same col
    elif coords1[1] == coords2[1]:
        cipher_text.append(table[(coords1[0] + 1) % 5][coords1[1]])
        cipher_text.append(table[(coords2[0] + 1) % 5][coords2[1]])

    # Intersection
    else:
        cipher_text.append(table[coords1[0]][coords2[1]])
        cipher_text.append(table[coords2[0]][coords1[1]])

cipher_text = ''.join(cipher_text)
print('Cipher Text: ', cipher_text)
print('---------------------------------------------')