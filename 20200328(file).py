"""
count = 0
score = 0

for student in range(1,6):
    print("Enter the score of student", student, ":", end = " ")
    #python print 自带回车
    score = int(input())

    if score >= 90:
        count += 1

print(count, "student(s) scored at least 90")
"""	





"""
sum = 0
score = 0

for student in range(1,5):
    print("Enter the score of student", student,":", end = " ")
    score = int(input())

    sum += score

print("the sum of students' score is =", sum)
"""




"""
maxSoFar = int(input("Enter a number: "))

for count in range(2,6):
    num = int(input("Enter the next number: "))

    if num > maxSoFar:
        maxSoFar = num

print("The maximum number is:", maxSoFar)

"""




"""
numRows = int(input("Enter the number of rows: "))

for count in range(1, numRows + 1):
    print(" " * (numRows - count), end = " ")
    print("*" * count)
"""




"""
numRows = int(input("Enter the number of rows: "))

for row in range(1, numRows + 1):
    for space in range(numRows-row, 0, -1):
        print(" ", end = "")
    for star in range(1, row+1):
        print("*", end = "")
    print()
"""


#Tutorial 2B


"""
#2
Name = input("Enter your name: ")

for count in range(1,11):
    print(Name)
"""

"""
#3

for num in range(1,129):
    value = str(chr(num))
    print("%4d%10s" % (num, value))
"""

"""
#4

testString = input("Enter a word: ")

for char in testString:
    print("%4s%10d" % (char, ord(char)))
"""

"""
#5

word = input("Enter a sentence: ")
count = 0

for char in word:
    if char == " ":
        count += 1

print("The number of spaces is =", count)
"""

"""
#6

sum = 0

num = int(input("Enter the number of iterations: "))

for count in range(0, num):
    approx = 1 / (2*count + 1)
    if (count % 2) != 0:
        approx = approx * -1
    sum += approx

print(sum)
"""

"""
#7

sum = 0
days = 0

for count in range(1,8):
    temp = int(input("Enter today's temperature: "))
    if temp > 0:
        sum += temp
        days += 1
    if count == 1 and temp < 0:
        days = 1

aveTemp = sum / days

print("The average noon temperature is:", aveTemp)
"""

"""
#8a

sum = 0

for num in range(1,101):
    sum += num ** 2

print(sum)
"""

"""
#8b
sum = 0
    
num = int(input("Enter the number of integers: "))

for count in range(1, num + 1):
    sum += count ** 2

print(sum)
"""

"""
#9

maxArea = 0

print("%8s%19s" % ("Length", "Area"))

for length in range(10,46):
    area = length * ((100 - (2 * length)) / 2)
    if area > maxArea:
        maxArea = area
        
    print("%8d%19d" % (length, area))

print("Maximum area is", round(maxArea))
"""

#Multiplication Table
"""
#10

column = int(input("Enter number of columns: "))

for i in range(0, column + 1):
    print(i, "\t", end = "")
print()

for j in range(1, column + 1):
    print(j, end = "\t")
    for k in range(1, j + 1):
        print(k * j, "\t", end = "")
    print("\n")
"""

#while loop

#using a y or n 
"""
sum = 0
ans = 'y'

while (ans == "y") or (ans == "Y"):
    num = int(input("Enter number: "))
    sum += num
    ans = input("type y to continue, n to stop: ")
    
print("The sum is", sum)
"""
#using a phony value -1
"""
sum = 0

num = int(input("enter number or -1 to stop: "))

while num != -1:
    sum += num
    num = int(input("enter number or -1 to stop: "))

print("The sum is", sum)
"""

"""    
sum = 0
n = 2

while sum <= 1000:
    n += 10
    sum += n * n

print("Sum first goes over 1000 when you add", n, "squared")
print("Sum is", sum)
"""

"""
capital = input("Enter the capital of Indonesia: ")

while capital != "Jakarta":
    for count in range(3):
        capital = input("Enter the capital of Indonesia: ")
        count += 1
        if capital == "Jakarta":
            print("Nice work. You got it on try", count)
    else:
        print("You did not get it in 3 tries")
        print("The correct answer is Jakarta")

if capital == "Jakarta":
    print("Nice work. You got it on try", count)
"""

"""
correct = False
tries = 0

#while loop condition must always be true

while not correct and tries < 3:
    capital = input("Enter capital of Indonesia: ")
    tries += 1
    if capital == "Jakarta":
        correct = True
        # break while loop by giving "False" condition

if correct:
    print("Nice work. You got it on try", tries)
else:
    print("You did not get it in 3 tries")
""" 
