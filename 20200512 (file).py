#6 Projects
#6
'''
import os, os.path

def menu():
    print("1 List the current directory \n" \
          "2 Move up \n" \
          "3 Move down \n" \
          "4 Number of files in the directory \n" \
          "5 Size of the directory in bytes \n" \
          "6 Search for a filename \n" \
          "7 View contents of a file \n" \
          "8 Quit the program \n")
    
def main():
    print(os.getcwd())
    menu()
    command = acceptCommand()
    runCommand(command)
    if command == "8":
        print("Have a nice day!")
    else:
        main()

def acceptCommand():
    command = input("Enter a number: ")
    if command in "12345678":
        return command
    else:
        print("Please enter a correct number")
        return acceptCommand()

def runCommand(command):
    if command == "1":
        print("Below is the list of current directory")
        listCurrentDir(os.getcwd())

    elif command == "2":
        moveUp()
        print("You have moved to the previous directory")

    elif command == "3":
        moveDown(os.getcwd())

    elif command == "4":
        print("The total number of files is", \
              countFiles(os.getcwd()))

    elif command == "5":
        print("The total number of bytes is", \
              sizeCWD(os.getcwd()))

    elif command == "6":
        target = input("Enter the search string: ")
        fileList = searchFile(target, os.getcwd())
        if not fileList:
            print("String not found")
        else:
            for f in fileList:
                print(f)
                
    elif command == "7":
        print(fileContent(os.getcwd()))
        
    print()

def listCurrentDir(dirName):
    lyst = os.listdir(dirName)
    for element in lyst:
        print(element)

def moveUp():
    os.chdir("..")
    
def moveDown(currentDir):
    name = input("Enter the name of directory: ")
    if os.path.exists(currentDir + os.sep + name) and \
       os.path.isdir(name):
        os.chdir(name)
        print("You have moved to the next directory")
        
    else:
        print("ERROR: The directory does not exist")

def countFiles(path):
    num = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            num += 1
        else:
            os.chdir(element)
            num += countFiles(os.getcwd())
            os.chdir("..")
            #remember to move back up the directory
    return num

def sizeCWD(path):
    size = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            size += os.path.getsize(element)
        else:
            os.chdir(element)
            size += sizeCWD(os.getcwd())
            os.chdir("..")
    return size

def searchFile(target, path):
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
        else:
            os.chdir(element)
            files.extend(searchFile(target, os.getcwd()))
            os.chdir("..")
    return files

def fileContent(path):
    print(os.listdir())
    name = input("Enter the name of a file to be viewed: ")
    if os.path.exists(name) and os.path.isfile(name):
        with open(name, "r") as f:
            text = f.read()
            return text
    else:
        print("Error. Please enter the correct filename")
        fileContent(path)

main()
'''

#7
'''
import os, os.path

def content(curDir):
    with open(curDir, 'r', encoding="utf8", errors='ignore') as f:
        text = f.read()
        return text

def function(pathName, file = []):
    if os.path.isfile(pathName):
        file.append(os.path.basename(pathName) + '\n' + content(pathName))
    else:
        for element in os.listdir(pathName):
            curDir = os.path.join(pathName, element)
            if os.path.isfile(curDir):
                file.append(element + '\n' + content(curDir) + '\n' + '\n')
            else:
                pathName = curDir
                function(pathName, file)
                head, tail = os.path.split(pathName)
                pathName = head
    return "".join(file)

def main():
    pathName = input("Enter a path name: ")
    if os.path.exists(pathName):
        print(function(pathName))
    else:
        print("Error. Please enter a correct path name")
        main()

main()
'''

#8
'''
def printAll(seq):
    if seq:
        print(seq[0])
        printAll(seq[1:])

def main():
    x = input("Enter a sequence: ")
    seq = x.split(" ")
    printAll(seq)

main()
'''

#9
'''
def readFile(fileName):
    f = open(fileName, 'r')
    numList = f.read().strip().split(",")
    numList = [int(num) for num in numList]
    print(numList)
    return numList
    
def average(numList):
    sum = 0
    for num in numList:
        sum += num
    average = sum / len(numList)
    return round(average, 2)

def main():
    fileName = input("Enter the file name: ")
    numList = readFile(fileName)
    print("The average of numbers is", average(numList))

main()
'''

