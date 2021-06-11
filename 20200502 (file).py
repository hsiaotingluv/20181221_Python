#Chapter 5 Projects
#1 stats.py
'''
def median(sentence):
    list = []
    for word in sentence.split():
        list.append(int(word))

    list.sort()

    if len(list) % 2 == 1:
        num = int(len(list) / 2)
        median = list[num]
    else:
        num = int(len(list) / 2)
        median = (list[num] + list[num - 1]) / 2

    return "The median is " + str(median)

def mode(sentence):
    list = []
    for word in sentence.split():
        list.append(word)
        
    dictionary = {}
    for num in list:
        number = dictionary.get(num, None)
        if number == None:
            dictionary[num] = 1
        else:
            dictionary[num] = number + 1

    theMaximum = max(dictionary.values())

    for key in dictionary:
        if dictionary[key] == theMaximum:
            return "The mode is " + key

def mean(sentence):
    list = []
    for word in sentence.split():
        list.append(int(word))
    sum = 0

    for num in list:
        sum += num

    mean = sum / len(list)
    return "The mean is " + str(mean)

def main():
    sentence = input("Enter a set of numbers or 'quit' to quit: ")

    while sentence.lower() != "quit":
        calculation = input("Compute median / mode / mean: ")
        
        if calculation.lower() == "median":
            print(median(sentence))

        elif calculation.lower() == "mode":
            print(mode(sentence))

        elif calculation.lower() == "mean":
            print(mean(sentence))

        else:
            print("Please enter a valid mode.")
            continue
                
        sentence = input("Enter a set of numbers or 'quit' to quit: ")

main()
'''

#2
'''
fileName = input("Enter the file name: ")
f = open(fileName, "r")
list = []
dictionary = {}

line = f.readline().strip()

while line != "":
    list.append(line)
    line = f.readline().strip()

for i in range(1, len(list) + 1):
    dictionary[i] = list[i - 1]

print("The number of lines is", len(list))
num = int(input("Enter a line number to print or 0 to quit: "))

while num != "0":
    print("The", num, "line is:", dictionary[num])
    num = int(input("Enter a line number to print or 0 to quit: "))

f.close()
'''

#3
'''
import random

def getWords(fileName):
    f = open(fileName, "r")
    list = f.read().splitlines()
    f.close() #to reset cursel
    return tuple(list)

def sentence(dictionary):
    return nounPhrase(dictionary) + " " + verbPhrase(dictionary)

def nounPhrase(dictionary):
    return random.choice(dictionary["articles"]) + " " + \
           random.choice(dictionary["nouns"])

def verbPhrase(dictionary):
    return random.choice(dictionary["verbs"]) + " " + \
           nounPhrase(dictionary) + " " + \
           prepositionalPhrase(dictionary)

def prepositionalPhrase(dictionary):
    return random.choice(dictionary["prepositions"]) + \
           " " + nounPhrase(dictionary)

def main():
    dictionary = {}
    for count in range(4):
        fileName = input("Enter the file name to import: ")
        x = getWords(fileName)
        #temporary variable x will change value after every run of getWords
        fileName = fileName.strip(".txt")
        dictionary[fileName] = x
        print(dictionary)

    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence(dictionary))

main()
'''
