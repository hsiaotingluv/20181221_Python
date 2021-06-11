#Chapter 4 Strings and Text Files
#Chapter 4 Projects

#encrypt.py
#1
'''
plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""

for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - \
                        (ord('z') - ordvalue + 1)
    code += chr(cipherValue)

print(code)
'''

#decrypt.py
#2
'''
code = input("Enter the code text: ")
distance = int(input("Enter the distance value: "))
plainText = ""

for ch in code:
    if ch.isalpha() == True:
        ordvalue = ord(ch)
        cipherValue = ordvalue - distance
        
        if cipherValue < ord('a'):
            cipherValue = ord('z') - \
                          (distance + (ord('a') - ordvalue - 1))
    else:
        cipherValue = ord(ch)

    plainText += chr(cipherValue)

print(plainText)
'''

#Hacking CAESAR CIPHER with brute force

'''
message = 'GUVF VF ZL FRPERG ZRFFNTR.'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translated = ''

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num -= key    #decode is always minus

            if num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]

        else:
            translated += symbol

    print("Key #%s: %s" % (key, translated))
'''


#3
'''
file = open("test.txt", "r")
distance = int(input("Enter the distance value: "))
code = ""


for line in file:
    for char in line:
        ordvalue = ord(char)
        cipherValue = ordvalue + distance
        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - \
                        (ord('z') - ordvalue + 1)
        code += chr(cipherValue)
    code += '\n'

print(code)

file.close()
'''

#Hacking CAESAR CIPHER with brute force
'''
text = input("Enter the code to encrypt: ")
text = text.lower()

distance, translated = 10, ""

for ch in text:
    if ch.isalpha() == True:
        ordvalue = ord(ch)
        cipherValue = ordvalue + distance
        
        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - \
                          (ord('z') - ordvalue + 1)
    else:
        cipherValue = ord(ch)
        
    translated += chr(cipherValue)

print(translated)
print()

text = input("Enter the code to decrypt: ")
for distance in range (1, 27):
    translated = ""

    for ch in text:
        if ch.isalpha() == True:
            ordvalue = ord(ch)
            cipherValue = ordvalue - distance
        
            if cipherValue < ord('a'):
                cipherValue = ord('z') - \
                              (distance + (ord('a') - ordvalue - 1))
        else:
            cipherValue = ord(ch)

        translated += chr(cipherValue)

    print(distance, translated)
'''
