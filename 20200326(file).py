"""
i = 1
while i < 5:
	print("循环内，i的值是", i)
	if i == 2:
            break
        i += 1
else:
    print("循环外，i的值是", i)"""





"""day = 1
while day <= 7:
    answer = input("今天有好好学习吗？")
    if answer != "有":
        print("你失败了，真失望！")
        break
    day += 1
else:
    print("非常棒，你已经坚持了7天连续学习！")
"""





"""
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(j, "*", i, "=", j * i, end = " ")
        j += 1
    print()
    i += 1
"""





"""
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(i, "*", j, "=", i * j, end = "     ")
        j += 1
    print()
    i += 1
"""




"""
day = 1
hour = 1
while day <= 7:
    while hour <= 8:
        print("今天我一定要坚持学习8个小时！")
        hour += 1
        if hour > 1:
            break
    day += 1
"""




"""
score = int(input("Enter your score: "))
if score >= 85:
    print(Band1)
elif score >=70:
    print(Band2)
elif score >=0:
    print(Band3)
else score > 100 or < 0:
    print(Error. Please enter a number between 0 to 100)
"""



"""
x = "apple"
y = "banana"

numx = ord('a')
numy = ord('b')

if numx > numy:
    print(y)
    print(x)
else:
    print(x)
    print(y)
"""




"""
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
sum = 0
for count in range (lower, upper + 1):
    sum = sum + count
print(sum)
"""




"""
startb = 10000.00
endb = 10000.00
year = 0
intr = 0.05

for count in range (5):
    if count == 0:
        print("%5s%20s%15s%20s" % ("Year", "Starting balance", "Interest", "Ending balance"))
        #should write this line before for, if not it will run 5 times.
    year += 1
    startb = round((endb + count * intr), 2)
    interest = round((startb * intr), 2)
    endb = round((startb + interest), 2)
    print("%5s%20s%15s%20s" % (year, startb, interest, endb))

qn1: how to standardise all decimal points?
    float dont need to round, it already has decimal
    by default, float has only 1 decimal point
    to have 2 decimal points, add .2f in the formatting line
qn2: how to round up/down correctly?
    just put round()
qn3: isnt range(5) suppose to run 5 rounds only? why are there 6 rows?
    
"""



"""
start = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = float(input("Enter the rate as a %: "))
totalinterest = 0
#total_interest / TotalInterest by convention

print("%5s%20s%15s%20s" % ("Year", "Starting balance", "Interest", "Ending balance"))

for year in range (1, years + 1):
#year is a variable, years is a constant
    interest = start * rate / 100
    end = start + interest
    print("%5d%20.2f%15.2f%20.2f" % (year, start, interest, end))
    start = end
    totalinterest += interest

end = round(end, 2)
totalinterest = round(totalinterest, 2)
print("Ending balance: $",end)
print("Total interest earned: $",totalinterest)
"""
        
