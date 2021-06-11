#Chapter 5 Projects
#6 decimal converter
'''
def decimalToRep(decimal, base):
    converted = 0
    i = 1

    while decimal != 0:
        converted += (decimal % base) * i
        decimal = int(decimal / base) 
        i = i * 10

    return "The number in base " + str(base) + " is: " + str(converted)

def decimalToHex(decimal, base):
    converted = ""
    dictionary = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, \
                  "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    b = 0
    a = decimal
    
    while a > 1:
        a = decimal / 16 ** b
        y = b
        b += 1
            
    for i in range(y - 1, -1, -1):
        hex = int(decimal / (16 ** i))

        for x, y in dictionary.items():
            if y == hex:
                converted += x
                
        decimal = (decimal % (16 ** i))
        
    return "The number in base 16 is: " + str(converted)

def main():
    x = input("Enter a decimal integer and the base of the converted number" + \
              " or 'quit' to quit: ")

    while x != "quit":
        decimal, base = x.split(",")
        base = int(base)
        decimal = int(decimal)
        if base == 16:
            print(decimalToHex(decimal, base))
        else:
            print(decimalToRep(decimal, base))
            
        x = input("Enter a decimal integer and the base of the converted number" + \
                  " or 'quit' to quit: ")

main()
'''

#7

'''
fileName = input("Enter the name of a text file: ")
f = open(fileName, 'r')

text = f.read().split()
text = sorted(text, key = str.lower)
print(text)

f.close()
'''

#8
'''
import string

fileName = input("Enter the name of a text file: ")
f = open(fileName, 'r')

s = f.read().lower()

#remove all punctuations from text
table = str.maketrans(dict.fromkeys(string.punctuation))  
new_s = s.translate(table)  

wordList = new_s.split()
wordList.sort()

dictionary = {}

print("%10s%20s" % ("words", "frequencies"))

for word in wordList:
    frequency = dictionary.get(word, None)
    if frequency == None:
        dictionary[word] = 1
    else:
        dictionary[word] = frequency + 1

words = list(dictionary.keys())
frequencies = list(dictionary.values())

for i in range(len(dictionary)):
    print("%10s%20s" % (words[i], frequencies[i]))

f.close()
'''
