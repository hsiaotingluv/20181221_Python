#Chapter 6 Case Study
#Gathering information from a File System
'''
import os, os.path

def menu():
    print("1 List the current directory \n" \
          "2 Move up \n" \
          "3 Move down \n" \
          "4 Number of files in the directory \n" \
          "5 Size of the directory in bytes \n" \
          "6 Search for a filename \n" \
          "7 Quit the program \n")
    
def main():
    print(os.getcwd())
    menu()
    command = acceptCommand()
    runCommand(command)
    if command == "7":
        print("Have a nice day!")
    else:
        main()

def acceptCommand():
    command = input("Enter a number: ")
    if command in "1234567":
        return command
    else:
        print("Please enter a correct number")
        return acceptCommand()

#print all outcomes here rather than in the function
#list clearly all possible outcomes
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

main()
'''

#Chapter 6 notes: Design with functions
'''
#Module Variables, Parameters, and Temporary
1. Module variables: introduced at the level of the module
2. Parameters: behaves like a variable, introduced in a function or method header
3. Temporary variables: introduced in the body of a function
4. Method names: always uses an object, followed by a dot and the method name

#temporary variable < module variable
functions cannot assign new value to a module variable
temporary variable of the same name is created within the function
During the call of f, storage exists for both variables,
so their values remain distinct

#example of temporary variable vs module variable
x = 5
def f():
    x = 10 # Attempt to reset x
f() # Does the top-level x change?
print(x) # No, this displays 5
When the function f is called, it does not assign 10 to the module variable x;
instead, it assigns 10 to a temporary variable x.

#Using Keywords for Default and Optional Arguments
#Benefits: simplify design and make functions more general
When the function is called without default arguments or keyword arguments,
their default values are automatically assigned to them.
When the function is called with these arguments,
the default values are overridden by the caller’s values.

#example of using default argument
def repToInt(repString, base = 2):
   """Converts the repString to an int in the base and returns this int."""
    decimal = 0
    exponent = len(repString) - 1
    for digit in repString:
        decimal = decimal + int(digit) * base ** exponent
        exponent -= 1
    return decimal

>>> repToInt("10", 8) # Override the default to here
8
>>> repToInt("10", 2) # Same as the default, not necessary
2
>>> repToInt("10")    # Base 2 by default
2

#Ways to supply default arguments when using functions
1. By position: values are supplied in the order in which the arguments
occur in the function header. Defaults are used for any arguments that are omitted.
2. By keyword. In this case, one or more values can be supplied in any order, using
the syntax <key> = <value> in the function call.

#example of ways to supplying default arguments
>>> def example(required, option1 = 2, option2 = 3):
        print(required, option1, option2)
>>> example(1)                # Use all the defaults
1 2 3
>>> example(1, 10)            # Override the first default
1 10 3
>>> example(1, 10, 20)        # Override all the defaults
1 10 20
>>> example(1, option2 = 20)  # Override the second default
1 2 20
>>> example(1, option2 = 20, option1 = 10)     # In any order
1 10 20

#Higher-Order Functions

#Type 1: mapping
#benefits:
1. single line to replace for loop, remove redundancy, eliminate a loop
2. conversion to list is only needed for viewing, map object can be passed directly
to another map function to perform further transformations of the data

#example of mapping shortening code
#Method 1: using a list and a for loop
def changePerson(sentence):
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))

    return " ".join(replyWords)

#Method 2: using mapping
def changePerson(sentence):
    def getWord(word):
        return replacements.get(word, word)
    return " ".join(map(getWord, sentence.split())

#Type 2: filtering
>>> def odd(n): return n % 2 == 1
>>> list(filter(odd, range(lO)))
[1, 3, 5, 7, 9]            

#Type 3: reducing                   
>>> from functools import reduce
>>> def add(x, y): return x + y
>>> data = [1, 2, 3, 4]
>>> reduce(add, data)
10

#lambda <argname-1, ..., argname-n>: <expression>
#benefit: define a function "on the fly"
                    
#example of lambda
>>> data = [1, 2, 3, 4]
>>> reduce(lambda x, y: x + y, data) # Produce the sum
10

#example of using range, reduce, lambda (simplified ver)
def summation(lower, upper):
    if lower > upper:
        return 0
    else:
        return reduce(lambda x, y: x + y,
                      range(lower, upper + 1))

#jump tables
#benefits: simplify code, easy to maintain
#assumptions: command string is a key in the jumpTable, function expects no arguments

#example of jump tables
def runCommand(command):    # How simple can it get?
    jumpTable[command]()

jumpTable = {}
jumpTable['1'] = insert()
jumpTable['2'] = replace()
jumpTable['3'] = remove()
'''
