#Chapter 3: strings and text files

#read file

'''
name = "Hsiao Ting"

for index in range(len(name)):
    print(index, name[index])
'''

'''
file = open("test.txt","r')

sizeToRead = 100

content = file.read(sizeToRead)

    while len(content) > 0: #stops when the content in the file ends
        print(content, end = " ")
        content = file.read(sizeToRead)
'''

'''
file = open("test.txt","r')

sizeToRead = 100

content = file.read(sizeToRead)
print(content)

file.seek(0) #goes back to the 0th character

content = file.read(sizeToRead)
print(content)

#prints the first 10 char twice
'''

#write a copy of a file

'''
rFile = open("test.txt","r')
wFile = open("testcopy.txt","w')

for line in  rFile:
    wFile.write(line)

rFile.close()
wFile.close()
'''

#write file
#safer way to read file

'''
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open("oceans.txt", "w") as file:
    for ocean in oceans:
        file.write(ocean)
        file.write("\n")
'''

'''
import random

f = open("integers.txt", "w")

for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + "\n")

f.close()
'''

#append file

'''
with open ("oceans.txt", "a") as f:
    file.write("=")
'''

#readline

'''
f = open("myfile.txt", "w")
f.write("First line. \nSecond line.\n")

f = open("myfile.txt", "r")
line = f.readline()

while line != "":
    print(line)
    line = f.readline()

f.close()
'''

#reading numbers from file

'''
Text file "Integers1.txt"

10
20
40
60

f = open("Integers1.txt", "r")
sum = 0

for line in f:
    line = line.strip()
    number = int(line)
    sum += number

print("The sum is", sum)
'''

'''
Text file "Integers2.txt"

10 20
40 60

f = open("Integers2.txt", "r")

for line in f:
    wordlist = line.split()
    for word in wordlist:
        number = int(word)
        sum += number

print("The sum is", sum)
'''

'''
file = open("test.txt", "r")

for line in file:
    sentences = line.split(".")

for word in sentences:
    words = word.split(" ")

for char in word:
    chars = char.split()

file.close()
'''

file = open("integers.txt", "r")


