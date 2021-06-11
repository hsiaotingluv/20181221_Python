#Chapter 6 Projects
#1 Newton’s method for approximating square roots
'''
import math

def newton(x):
   tolerance = 0.000001
   estimate = 1.0

   while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break

   return estimate

def main():
    x = input("Enter a number or press 'enter' to quit: ")
    while x != "":
        x = float(x)
        print("The program's estimate is:", newton(x))
        print("Python's estimate is:", math.sqrt(x))
        print()
        x = input("Enter a number or press 'enter' to quit: ")

main()
'''  

#2, 3 newton method + recursive function + default argument
'''
import math

def newton(x, estimate = 1):
    tolerance = 0.000001

    if abs(x - estimate ** 2) <= tolerance:
        return estimate

    else:
        return newton(x, (estimate + x / estimate) / 2)

def main():
    x = input("Enter a number or press 'enter' to quit: ")
    while x != "":
        x = float(x)
        print("The program's estimate is:", newton(x, estimate = 1))
        print("Python's estimate is:", math.sqrt(x))
        print()
        x = input("Enter a number or press 'enter' to quit: ")

main()
'''

#4 multiple functions
'''
import math

def newton(x, estimate = 1):

    while True:
        estimate = improveEstimate(x, estimate)
        last = estimate
        if limitReached(x, last) == True:
            break
    
    return estimate
        
def limitReached(x, last):
    return abs(x - last ** 2) <= 0.000001
        
def improveEstimate(x, estimate):
    return (estimate + x / estimate) / 2

def main():
    x = input("Enter a number or press 'enter' to quit: ")
    while x != "":
        x = float(x)
        print("The program's estimate is:", newton(x, estimate = 1))
        print("Python's estimate is:", math.sqrt(x))
        print()
        x = input("Enter a number or press 'enter' to quit: ")

main()
'''

#5
'''
def check(isSorted):
    for i in range(1, len(isSorted)):
        if isSorted[i - 1] > isSorted[i]:
            return "False"
        
    return "True"

def main():
    while True:
        value = input("Enter a list of sorted items or 'enter' to quit: ")
        if value == '':
            break
        isSorted = value.split(",")
        print(check(isSorted))

main()
'''

