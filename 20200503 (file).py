#Chapter 5 Projects
#4
'''
import random

def getWords(fileName):
    f = open(fileName, "r")
    list = f.read().splitlines()
    f.close() #to reset cursel
    return tuple(list)

def sentence(dictionary):
    probability = random.randint(1, 2)
    if probability == 1:
        return nounPhrase(dictionary) + " " + verbPhrase(dictionary)
    else:
        return nounPhrase(dictionary) + " " + verbPhrase(dictionary) + \
               " " + random.choice(dictionary["conjunctions"]) + " " + \
               nounPhrase(dictionary) + " " + verbPhrase(dictionary)

def nounPhrase(dictionary):
    probability = random.randint(1, 2)
    if probability == 1:
        return random.choice(dictionary["articles"]) + " " + \
               random.choice(dictionary["nouns"])
    else:
        return random.choice(dictionary["articles"]) + " " + \
               random.choice(dictionary["adjectives"]) + " " + \
               random.choice(dictionary["nouns"])

def verbPhrase(dictionary):
    probability = random.randint(1, 2)
    if probability == 1:
        return random.choice(dictionary["verbs"]) + " " + \
               nounPhrase(dictionary) + " " + \
               prepositionalPhrase(dictionary)
    else:
        return random.choice(dictionary["verbs"]) + " " + \
               nounPhrase(dictionary)

def prepositionalPhrase(dictionary):
    return random.choice(dictionary["prepositions"]) + \
           " " + nounPhrase(dictionary)

def main():
    dictionary = {}
    for count in range(6):
        fileName = input("Enter the file name to import: ")
        x = getWords(fileName)
        #temporary variable x will change value after every run of getWords
        fileName = fileName.strip(".txt")
        dictionary[fileName] = x

    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence(dictionary))

main()
'''

#5 repToDecimal
'''
def repToDecimal(num, base):
    i, decimal = 1, 0
    num = int(num)
    
    while num != 0:
        decimal += (num % 10) * i
        num = int(num / 10)
        i = i * base
    return "The converted number is " + str(decimal)

def getNumbers(num, digit):
    dictionary = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, \
                  "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

    x = num[digit]
    x = (dictionary[str(x)])
    return x

def hexToDecimal(num):   
    decNum = 0
    power = len(num) - 1 
    
    for digit in range(len(num)):
        decNum += 16 ** power * getNumbers(num, digit)
        power -= 1
    return "The converted number is " + str(decNum)
    

def main():
    x = input("Enter a number and its base to convert to decimal, or 'quit' to quit: ")

    while x != 'quit':
        num = ""
        inputNum, base = x.split(",")
        base = int(base)

        for value in inputNum:
            if value in "0,1,2,3,4,5,6,7,8,9":
                num += value
            else:
                num += value.upper()
        
        if base == 16:
            print(hexToDecimal(num))
        else:
            print(repToDecimal(num, base))
        x = input("Enter a number and its base to convert to decimal, or 'quit' to quit: ")

main()
'''
