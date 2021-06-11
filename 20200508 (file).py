#Chapter 6 exercises
#1
'''
numbers = input("Enter a list of numbers: ")
numList = numbers.split(",")
absValues = []

for num in numList:
    absValues.append(str(abs(int(num))))
        
print("The absolute values are: ", ",".join(absValues))
'''

#1 using mapping
'''
inputList = map(int, input("Enter a list of numbers: ").split(','))

print("Absolute values are:", list(map(abs, inputList)))
'''

#2 using filtering
'''
inputList = map(int, input("Enter a list of numbers: ").split(','))
    
print(list(filter(lambda x: x > 0, inputList)))
'''

#3 using reducing
'''
from functools import reduce

data = ["hello", "world", "my name", "is", "hsiaoting"]
print(reduce(lambda x, y: x + " " + y, data))
'''

#4 default arguments
'''
def summation(lower, upper, step = 1, func = lambda x: x):
    return sum(map(func, range(lower, upper+1, step)))
'''

#loop vs recursion vs reduce
'''
recursion
benefits: simplify, easy to maintain, can call function multiple times at any place
cost: memory space

loop
benefits: less memory space
cost: redundancy, repetition, hard to maintain, can only call once

reduce
benefits: simplify
'''
