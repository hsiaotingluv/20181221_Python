#Chapter 4 Projects
#3 encrypt and decrypt a file
'''
f1 = open("encrypt.txt", "w")
text = input("Enter to encrypt: ")
text = text.lower()
distance = 10
code = ""

for ch in text:
    if ch.isalpha() == True:
        num = ord(ch)
        cipherValue = num + distance

        if cipherValue > ord("z"):
            cipherValue = ord("a") + distance - (ord("z") - num + 1)

    else:
        cipherValue = ord(ch)

    code += chr(cipherValue)

for line in code:
    f1.write(line)

f1.close()

f2 = open("decrypt.txt", "w")
f1 = open("encrypt.txt", "r")
text = f1.read()
translated = ""

for ch in text:
    if ch.isalpha() == True:
        num = ord(ch)
        cipherValue = num - distance

        if cipherValue < ord("a"):
            cipherValue = ord("z") - (distance + (ord("a") - num - 1))

    else:
        cipherValue = ord(ch)

    translated += chr(cipherValue)

f2.write(translated)

f2.close()
f1.close()
'''

#4 convert octal to decimal vise versa
'''
ans = input("choose to convert octal to decimal or vise versa: ")

if ans == "octal to decimal":
    octal = int(input("Enter an octal integer: "))

    i, decimal = 1, 0

    while octal != 0:
        decimal += (octal % 10) * i
        octal = int(octal / 10)
        i = i * 8

    print("The decimal number is", decimal)    


if ans == "decimal to octal":
    decimal = int(input("Enter a decimal integer: "))

    i, octal = 1, 0 

    while decimal != 0:
        octal += (decimal % 8) * i
        decimal = int(decimal / 8)
        i = i * 10

    print("The octal number is", octal)
'''  

# define a function
'''
def names():
    name = input("Enter your name: ")
    if set("aeiou").intersection(name.lower()):
        print("Your name contains a vowel.")
    else:
        print("Your name does not contain a vowel.")

    for letter in name:
        print(letter)
names()
'''

#5 shiftRight.py shiftLeft.py
'''
bitString = input("Enter a bit string: ")
mode = input("Enter to shiftLeft or shiftRight: ")
    
def shiftLeft(bitString):
    translated = bitString[1:] + bitString[:1]
    return translated

def shiftRight(bitString):
    translated = bitString[-1:] + bitString[:-1]
    return translated

if mode == "shiftLeft":
    print("The shifted bits is:", shiftLeft(bitString))
elif mode == "shiftRight":
    print("The shifted bits is:", shiftRight(bitString))
else:
    print("Please enter the correct mode.")
    mode = input("Enter to shiftLeft or shiftRight: ")
'''

#6 
#encrypt
'''
decimal = input("Enter a decimal to encrypt: ")
translated = ""

for num in decimal:
    cipherValue = ord(num) + 1
    
    i, bitString = 1, 0 

    while cipherValue != 0:
        bitString += (cipherValue % 2) * i
        cipherValue = int(cipherValue / 2)
        i = i * 10

    bitString = str(bitString)
    bitString = bitString[1:] + bitString[:1]
    translated += bitString + " "
    
print("The encrypted string is", translated)
'''

#7
#decrypt
'''
code = input("Enter a code to decrypt: ")
code = code.split(" ")
num, translated = "", ""

for bitString in code:
    shiftRight = bitString[-1:] + bitString[:-1]
    shiftRight = int(float(shiftRight))

    i, cipherValue = 1, 0
     
    while shiftRight != 0:
        cipherValue += (shiftRight % 10) * i
        shiftRight = int(shiftRight / 10)
        i = i * 2

    num = cipherValue - 1
    num = chr(num)
    translated += num 

print("The decrypted decimal is", translated)
'''

#8 copyfile.py
'''
f1 = open(input("Enter the file to copy: "), "r")
f2 = open(input("Enter the file to paste into: "), "a")

text = f1.read()

f2.write("\n\nThe copied text file\n\n")

for line in text:
    f2.write(line)

f1.close()
f2.close()
'''


#9 numberlines.py
'''
f1 = open(input("Enter the file to copy: "), "r")
f2 = open(input("Enter the file to paste into: "), "a")
text = f1.read()
count = 1

f2.write("\n\nThe copied text file\n\n")
f2.write("%-4s" % (str(count) + ">"))

for line in text:
    f2.write(line)
    if line == "\n":
        count += 1
        f2.write("%-4s" % (str(count) + ">"))
    
f1.close()
f2.close()
'''

