#median.py

fileName = input("Enter the filename: ")
f = open(fileName, "r")

numbers = []
for line in f:
    words = line.split()
    for char in words:
        numbers.append(float(char))

number.sort()
midpoint = len(numbers) // 2
print("The median is", end = " ")
if len(numbers) % 2 == 1:
    print(numbers[midpoint])
else:
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2)

f.close()


