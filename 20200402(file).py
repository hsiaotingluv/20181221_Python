#Assignment 2
'''
#1
x = int(input("Enter the length: "))
y = int(input("Enter another length: "))
z = int(input("Enter last length: "))

if x == y == z:
    print("This is an equilateral triangle")
else:
    print("This is not an equilateral triangle")
'''

'''
#2
num = 0
vowel = 0
word = input("Enter a word: ")

for char in word:
    num += 1
    if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
        vowel += 1

per = (vowel / num) * 100

print("The number of letters is", num)
print("The number of vowels is", vowel)
print("The percentage of vowels is", round(per, 2),"%")
'''

'''
#3
playerOne = input("Enter choice of player one: ")
playerTwo = input("Enter choice of player two: ")

if (playerOne == "P" and playerTwo == "R") or (playerOne == "R" and playerTwo == "S") or (playerOne == "S" and playerTwo == "P"):
    print("Player one is the winner")
elif ord(playerOne) == ord(playerTwo):
    print("The game is a tie")
elif (playerTwo == "P" and playerOne == "R") or (playerTwo == "R" and playerOne == "S") or (playerTwo == "S" and playerOne == "P"):
    print("Player two is the winner")
else:
    print("Error. Please enter 'P' 'S' or 'R'")
'''

'''
#4
num = int(input("Enter a positive integer: "))

for count in range(1, num + 1):
    if (count == 1 or count == num):
        print("* " * num * 2)
    else:
        print("* ", " " * (num * 2 - 3) * 2,"* ")
'''

'''
#5
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))

while B != 0 and A >= B:
    i = A % B
    print("The remainder is", i)
    A = B
    B = i
    print("The larger number is now", A, ", the smaller number is now", B)
    
while A != 0 and B >= A:
    j = B % A
    print("The remainder is", j)
    B = A
    A = j
    print("The larger number is now", B, ", the smaller number is now", A)

if A > B:
    print("The greatest common divisor is", A)
else:
    print("The greatest common divisor is", B)
'''

'''
#6

sum = 0
maxSum = 0
maxNum = 0

for count in range(100, 111):
    print(count, end = ": ")
    for num in range(1, count + 1):
        if count % num == 0:
            print(num, end = " ")
            sum += num
            
    if sum > maxSum:
        maxSum = sum
        maxNum = count
        
    print()
    print("sum of divisors is", sum)
    print()
    
print(str(maxNum) + " has maximum sum of divisors.")

#how to print which number has maximum sum of divisors??
'''

'''
#7
square = 0
cube = 0
sumSquare = 0
sumCube = 0
numCube = 0

for count in range (16):
    square = count ** 2
    cube = count ** 3
    sumSquare += square
    sumCube += cube
    
    if count == 0:
        print("%6s%10s%8s" % ("NUMBER", "SQUARE", "CUBE"))
    else:
        print("%6d%10d%8d" % (count, square, cube))

    if cube > 500:
        numCube += 1

if sumSquare > 2000:
    print("The sum of the squares is", sumSquare)
    print("The sum of the squares exceed 2000")
else:
    print("The sum of the squares is", sumSquare)
    
print("The sum of the cubes is", sumCube)
print(numCube, "number of cubes were greater than 500")
'''

'''    
#8
import random

money = float(input("Enter the amount of money you want to put into the pot: "))
num = 0
maxMoney = money

while money != 0:
    x = random.randint(1,6)
    y = random.randint(1,6)
    print(x, y)
    num += 1
    
    if x + y == 7:
        money += 4
    else:
        money -= 1

    if money > maxMoney:
        maxMoney = money

print("The number of rolls took is", num)
print("The maximum amount of money in the pot is", maxMoney)
'''

'''
#9 Version A
import random

num = random.randint(1,100)
guess = int(input("Enter your guess: "))
tries = 1

while guess != num:
    if guess > num:
        print("Too big")
    else:
        print("Too small")
    tries += 1
    guess = int(input("Enter your guess: "))

print("You've got it in", tries, "tries!")
'''

'''
#9 Version B
import random

num = int(input("Enter a number between 1 to 100: "))
guess = random.randint(1,100)
tries = 1
print(guess)

while guess != num:
    if guess > num:
        print("Too big")
    else:
        print("Too small")
    tries += 1
    guess = random.randint(1,100)
    print(guess)

print("The computer has got it in", tries, "tries!")
'''

'''
#10
numDist = 0
numPass = 0
ans = input("Enter y to continue, n to stop: ")

while ans == 'y':
    sum = 0
    for count in range(3):
        score = int(input("Enter the score: "))
        while score <= 0 or score >= 100:
            print("Invalid number! Enter a number between 0 to 100!")
            score = int(input("Enter the score: "))
        #error trapping loop
            
        sum += score
        if score >= 60:
            print("Passed")
        elif score < 60:
            print("Failed")
            
    ave = round(sum / 3)
    print("Your average score is", ave)

    if (ave >= 60):
        numPass += 1
    if ave >= 80:
        numDist += 1

    ans = input("Enter y to continue, n to stop: ")

print("Number of students passed is", numPass)
print("Number of students with average of at least 80 is", numDist)
'''
