'''
file = input("Enter the file name: ")
inputFile = open(file, "r")
text = inputFile.read()
text = text.lower()

sentences = text.count(".") + text.count("?") + \
            text.count("!") + text.count(":") + \
            text.count(";")

words = len(text.split())
vowels = ("aeiouy")
syllables = 0
previous = ""

for word in text.split():
    for char in word:
        if char in vowels:
            previous += char
        else:
            if previous != "":
                syllables += 1
            previous = ""

    if previous != "":
        syllables += 1
        previous = ""
           
    for ending in ["es", "ed", "e"]:
        if word.endswith(ending):
            syllables -= 1
        if word.endswith("le"):
            syllables += 1

index = 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)
grade = 0.39 * (words/sentences) + 11.8 * (syllables/words) - 15.59

print("There are", sentences, "sentences")
print("There are", words, "words")
print("There are", syllables, "syllables")
print("The Flesch index is", round(index))
print("The grade-level equivalent is", round(grade))

inputFile.close()
'''

#Tutorial 3

'''
#6

file = input("Enter a file name: ")
inputFile = open(file, "r")
text = inputFile.read()
count = 0

for line in inputFile:
    count += 1

print("The number of lines is", count)

inputFile.close()
'''

#7
'''
file = input("Enter a file name: ")
inputFile = open(file, "r")
text = inputFile.read()

wordList = text.split("\n")

num = 0
for word in wordList:
    if len(word) == 4:
        num += 1
    
print("The number of four-letter words is", num)

inputFile.close()
'''

#8
'''
file = open("test.txt", "r")
text = file.read()

intList = text.split("\n")

sum = 0
for integer in intList:
    sum += int(integer)

print("The average value is", sum / len(intList))

file.close()
'''

#Assignment 3

'''
#1

myString = input("Enter a sentence: ")
reverse = ""

for count in range(1, len(myString) + 1):
   reverse += myString[len(myString) - count]

print("The reverse is", reverse)
'''

'''
#2

myString = input("Enter a sentence: ")
reversedString = ""

for count in range(1, len(myString) + 1):
    reversedString += myString[len(myString) - count]

print("The reverse is", reversedString)
'''

'''
#3

f1 = input("Enter the file to copy: ")
fileOne = open(f1, "r")

f2 = input("Enter the file to paste: ")
fileTwo = open(f2, "a")

for line in fileOne.readlines():
    fileTwo.write(line)

fileOne.close()
fileTwo.close()
'''

'''
#4 dif.py
f1 = input("Enter the first file: ")
f2 = input("Enter the second file: ")

file1 = open(f1, "r")
file2 = open(f2, "r")

same, end = True, False

while same and not end:
    line1 = file1.readline().strip()
    line2 = file2.readline().strip()
    
    if line1 != line2:
        same = False
    
    elif line1 == "" and line2 == "":
        end = True

if end:
    print()
    print("Yes, they are the same")
else:
    print()
    print("No, they are not the same")
    print("File one:", line1)
    print("File two:", line2)

#problem: cannot tell if both files contain empty lines
'''

'''
#5

file = open("payment.txt","w")

file.write("%10s%15s%20s" % ("<last name>", "<hourly wage>", "<hours worked>"))
file.write("\n")
ans = input("Enter y to continue, n to stop: ")

while ans == "y":
    file.write("%10s%15s%20s" % ((input("Enter the last name: ")), \
                                (input("Enter the hourly wage: ")),\
                                (input("Enter the hours worked: "))))
    file.write("\n")
    ans = input("Enter y to continue, n to stop: ")

file.close()
'''  
