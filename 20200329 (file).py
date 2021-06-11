#Nested while loop (error trapping and robustness)
"""
maleSum = 0
femaleSum = 0
ans = 'y'

while (ans == 'y' or ans == 'Y'):
    point = int(input("Enter the point: "))
    sex = input("Enter sex: ")

    while (sex != 'm' and sex != 'f'):
        sex = input("Error. Enter sex (m or f): ")

    if sex == 'm':
        maleSum += point
    else:
        femaleSum += point

    ans = input("Type y to continue, n to stop: ")

print("Total points for the male team:", maleSum)
print("Total points for the female team:", femaleSum)
"""


#Tutorial 2C
"""
#1
factorial = 1
num = int(input("Enter an integer: "))
N = num

while N > 1:
    factorial *= N
    N -= 1

print("The factorial of", num, "is", factorial)
"""

'''
A = float(input("Enter number to find square root: "))
X = float(input("Enter approximation: "))
epsilon = float(input("Enter epsilon: "))

error = epsilon
while error >= epsilon:
    X = (X + A/X) / 2
    error = abs(X - A/X) #abs for absolute

print(X)
'''

'''
#2
approx = 0

A = float(input("Enter a positive integer for approximating the square root: "))

while A <= 0:
    print("Error. Please enter a postive real value.")
    A = float(input("Enter a positive integer for approximating the square root: "))

X = float(input("Enter a positive approximation: "))

while X <= 0:
    print("Error. Please enter a postive real value.")
    X = float(input("Enter a positive approximation: "))

epilson = float(input("Enter the specified error allowance, epsilon: "))

while epilson <= 0:
    print("Error. Please enter a postive real value.")
    epilson = float(input("Enter the specified error allowance, epsilon: "))
    
approx = (X + A / X) / 2

while (X - A / X != epilson or A / X - X != epilson):
    X = approx
    approx = (X + A / X) / 2

print("The approximation square root of", A, "is", approx)
'''

"""
#3

ans = input("Enter item name or xyz to stop: ")
bill = 0

while ans != "xyz":
    price = float(input("Enter price per item: "))
    num = int(input("Enter quantity: "))
    sumPrice = price * num
    bill += sumPrice
    print(num, ans, "\t", "$", end = "")
    print("%.2f" % round(sumPrice, 2))
    ans = input("Enter item name or xyz to stop: ")

print("Total bill", "\t", "$", end = "")
print("%.2f" % round(bill, 2))
"""

'''
file = open("test.txt", "r")

text = file.readlines()
print(text)

file = open("test.txt", "r")
for line in file:
    line = line.strip() #remove \n #strip only the sides
    a, b, c = line.split(",") #split the variables between the ","
    print(a)

file.close()
'''

'''
file = open("test.txt", "w") #"w" will clear the file entirely

for i in range(4):
    file.write("Hello World") #can only write string
    file.write("!" * i)
    file.write("\n")

file.close() #must close the file
'''

