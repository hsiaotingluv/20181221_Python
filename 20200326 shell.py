Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> while True:
        answer = input("主人，我可以退出循环了吗？")
        if answer == "可以!":
                break

        
主人，我可以退出循环了吗？yes
主人，我可以退出循环了吗？yes
主人，我可以退出循环了吗？可以!
>>> while True:
        answer = input("主人，我可以退出循环了吗？")
        if answer == "可以!":
                break
        print("哎，好累～～～")

        
主人，我可以退出循环了吗？不行
哎，好累～～～
主人，我可以退出循环了吗？努力
哎，好累～～～
主人，我可以退出循环了吗？可以！
哎，好累～～～
主人，我可以退出循环了吗？可以!
>>> for
SyntaxError: invalid syntax
>>> i = 0
>>> while i < 10:
	i += 1
	print(i)

	
1
2
3
4
5
6
7
8
9
10
>>> while i < 10:
	i += 1
	if i % 2 == 0:
		continue
	print(i)

	
>>> 
>>> 
>>> while i < 10:
	i += 1
	if i % 2 == 0:
		continue
	print(i)

	
>>> while i < 10:
	i += 1
	if i % 2 == 0:
		continue
	print(i)

	
>>> 
>>> 
>>> i = 0
>>> while i < 10:
	i += 1
	if i % 2 == 0:
		continue
	print(i)

	
1
3
5
7
9
>>> i  = 1
>>> while i < 5:
	print("循环内，i的值是",1)
	1 += 1
	
SyntaxError: cannot assign to literal
>>> 
== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ==
循环内，i的值是 1
循环内，i的值是 2
循环内，i的值是 3
循环内，i的值是 4
循环外，i的值是 5
>>> i = 1
while i < 5:
	print("循环内，i的值是", i)
	if i == 2:
            break
        i += 1
else:
    print("循环外，i的值是", i)
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ==
今天有好好学习吗？有
今天有好好学习吗？有
今天有好好学习吗？有
今天有好好学习吗？有
今天有好好学习吗？有
今天有好好学习吗？有
今天有好好学习吗？有
非常棒，你已经坚持了7天连续学习！
>>> 
== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ==
今天有好好学习吗？又把
>>> 
== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ==
今天有好好学习吗？没有
你失败了，真失望！
>>> 
== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ==
1 * 1 = 1 
1 * 2 = 2 2 * 2 = 4 
1 * 3 = 3 2 * 3 = 6 3 * 3 = 9 
1 * 4 = 4 2 * 4 = 8 3 * 4 = 12 4 * 4 = 16 
1 * 5 = 5 2 * 5 = 10 3 * 5 = 15 4 * 5 = 20 5 * 5 = 25 
1 * 6 = 6 2 * 6 = 12 3 * 6 = 18 4 * 6 = 24 5 * 6 = 30 6 * 6 = 36 
1 * 7 = 7 2 * 7 = 14 3 * 7 = 21 4 * 7 = 28 5 * 7 = 35 6 * 7 = 42 7 * 7 = 49 
1 * 8 = 8 2 * 8 = 16 3 * 8 = 24 4 * 8 = 32 5 * 8 = 40 6 * 8 = 48 7 * 8 = 56 8 * 8 = 64 
1 * 9 = 9 2 * 9 = 18 3 * 9 = 27 4 * 9 = 36 5 * 9 = 45 6 * 9 = 54 7 * 9 = 63 8 * 9 = 72 9 * 9 = 81 
>>> 
== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ==
1 * 1 = 1 2 * 1 = 2 3 * 1 = 3 4 * 1 = 4 5 * 1 = 5 6 * 1 = 6 7 * 1 = 7 8 * 1 = 8 9 * 1 = 9 
1 * 2 = 2 2 * 2 = 4 3 * 2 = 6 4 * 2 = 8 5 * 2 = 10 6 * 2 = 12 7 * 2 = 14 8 * 2 = 16 9 * 2 = 18 
1 * 3 = 3 2 * 3 = 6 3 * 3 = 9 4 * 3 = 12 5 * 3 = 15 6 * 3 = 18 7 * 3 = 21 8 * 3 = 24 9 * 3 = 27 
1 * 4 = 4 2 * 4 = 8 3 * 4 = 12 4 * 4 = 16 5 * 4 = 20 6 * 4 = 24 7 * 4 = 28 8 * 4 = 32 9 * 4 = 36 
1 * 5 = 5 2 * 5 = 10 3 * 5 = 15 4 * 5 = 20 5 * 5 = 25 6 * 5 = 30 7 * 5 = 35 8 * 5 = 40 9 * 5 = 45 
1 * 6 = 6 2 * 6 = 12 3 * 6 = 18 4 * 6 = 24 5 * 6 = 30 6 * 6 = 36 7 * 6 = 42 8 * 6 = 48 9 * 6 = 54 
1 * 7 = 7 2 * 7 = 14 3 * 7 = 21 4 * 7 = 28 5 * 7 = 35 6 * 7 = 42 7 * 7 = 49 8 * 7 = 56 9 * 7 = 63 
1 * 8 = 8 2 * 8 = 16 3 * 8 = 24 4 * 8 = 32 5 * 8 = 40 6 * 8 = 48 7 * 8 = 56 8 * 8 = 64 9 * 8 = 72 
1 * 9 = 9 2 * 9 = 18 3 * 9 = 27 4 * 9 = 36 5 * 9 = 45 6 * 9 = 54 7 * 9 = 63 8 * 9 = 72 9 * 9 = 81 
>>> 
===================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ====================
1 * 1 = 1 1 * 2 = 2 1 * 3 = 3 1 * 4 = 4 1 * 5 = 5 1 * 6 = 6 1 * 7 = 7 1 * 8 = 8 1 * 9 = 9 
2 * 1 = 2 2 * 2 = 4 2 * 3 = 6 2 * 4 = 8 2 * 5 = 10 2 * 6 = 12 2 * 7 = 14 2 * 8 = 16 2 * 9 = 18 
3 * 1 = 3 3 * 2 = 6 3 * 3 = 9 3 * 4 = 12 3 * 5 = 15 3 * 6 = 18 3 * 7 = 21 3 * 8 = 24 3 * 9 = 27 
4 * 1 = 4 4 * 2 = 8 4 * 3 = 12 4 * 4 = 16 4 * 5 = 20 4 * 6 = 24 4 * 7 = 28 4 * 8 = 32 4 * 9 = 36 
5 * 1 = 5 5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25 5 * 6 = 30 5 * 7 = 35 5 * 8 = 40 5 * 9 = 45 
6 * 1 = 6 6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36 6 * 7 = 42 6 * 8 = 48 6 * 9 = 54 
7 * 1 = 7 7 * 2 = 14 7 * 3 = 21 7 * 4 = 28 7 * 5 = 35 7 * 6 = 42 7 * 7 = 49 7 * 8 = 56 7 * 9 = 63 
8 * 1 = 8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64 8 * 9 = 72 
9 * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81 
>>> 
===================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ====================
1 * 1 = 1     1 * 2 = 2     1 * 3 = 3     1 * 4 = 4     1 * 5 = 5     1 * 6 = 6     1 * 7 = 7     1 * 8 = 8     1 * 9 = 9     
2 * 1 = 2     2 * 2 = 4     2 * 3 = 6     2 * 4 = 8     2 * 5 = 10     2 * 6 = 12     2 * 7 = 14     2 * 8 = 16     2 * 9 = 18     
3 * 1 = 3     3 * 2 = 6     3 * 3 = 9     3 * 4 = 12     3 * 5 = 15     3 * 6 = 18     3 * 7 = 21     3 * 8 = 24     3 * 9 = 27     
4 * 1 = 4     4 * 2 = 8     4 * 3 = 12     4 * 4 = 16     4 * 5 = 20     4 * 6 = 24     4 * 7 = 28     4 * 8 = 32     4 * 9 = 36     
5 * 1 = 5     5 * 2 = 10     5 * 3 = 15     5 * 4 = 20     5 * 5 = 25     5 * 6 = 30     5 * 7 = 35     5 * 8 = 40     5 * 9 = 45     
6 * 1 = 6     6 * 2 = 12     6 * 3 = 18     6 * 4 = 24     6 * 5 = 30     6 * 6 = 36     6 * 7 = 42     6 * 8 = 48     6 * 9 = 54     
7 * 1 = 7     7 * 2 = 14     7 * 3 = 21     7 * 4 = 28     7 * 5 = 35     7 * 6 = 42     7 * 7 = 49     7 * 8 = 56     7 * 9 = 63     
8 * 1 = 8     8 * 2 = 16     8 * 3 = 24     8 * 4 = 32     8 * 5 = 40     8 * 6 = 48     8 * 7 = 56     8 * 8 = 64     8 * 9 = 72     
9 * 1 = 9     9 * 2 = 18     9 * 3 = 27     9 * 4 = 36     9 * 5 = 45     9 * 6 = 54     9 * 7 = 63     9 * 8 = 72     9 * 9 = 81     
>>> 
= RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py
今天我一定要坚持学习8个小时！
今天我一定要坚持学习8个小时！
今天我一定要坚持学习8个小时！
今天我一定要坚持学习8个小时！
今天我一定要坚持学习8个小时！
今天我一定要坚持学习8个小时！
今天我一定要坚持学习8个小时！
>>> for i in range(3)
SyntaxError: invalid syntax
>>> for i in range(3):
	if i == 0L
	
SyntaxError: invalid syntax
>>> x = 1
>>> y = 2
>>> for i in range(3):
	if i == 0:
		print("%7s%10s" % ("Name", "Class"))
	x += 1
	y += 2
	print("%7d%10d" % (x, y))

	
   Name     Class
      2         4
      3         6
      4         8






>>> for i in range(3):
	if i == 0:
		print("%7s%10s" % ("Name", "Class"))
	x += 1
	y += 2
	print("%7d%10d" % (x, y))
	break

   Name     Class
      5        10
>>> for i in range(3):
	if i == 0:
		print("%7s%10s" % ("Name", "Class"))
	x += 1
	y += 2
	print("%7d%10d" % (x, y))

	
   Name     Class
      6        12
      7        14
      8        16
>>> for i in range(3):
	x += 1
	y += 2
	print("%7d%10d" % (x, y))

	
      9        18
     10        20
     11        22
>>> for i in range(3):
	x += 1
	y += 2
	print("%7d%10d" % (x, y))

	
     12        24
     13        26
     14        28
>>> for i in range(1,3):
	x += 1
	y += 2
	print("%7d%10d" % (x, y))

	
     15        30
     16        32
>>> score = input("Enter your score: ")
Enter your score: 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Documents/20200326(newproj).py", line 89, in <module>
    x = apple
NameError: name 'apple' is not defined
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Documents/20200326(newproj).py", line 89, in <module>
    x = apple
NameError: name 'apple' is not defined
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
apple
banana
>>> product = 1
>>> for count in range(4):
	product = product * (count + 1)

	
>>> product
24

>>> for count in range(2):
	product = product * (count + 1)

	
>>> 
>>> product = 1
>>> for count in range(2):
	product = product * (count + 1)

	
>>> product
2
>>> for count in range(2)
SyntaxError: invalid syntax
>>> for count in range(2):
	print count
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(count)?
>>> for count in range(2):
	print(count)

	
0
1
>>> for count in range(3):
	print(count)

	
0
1
2
>>> product = 1
>>> for count in range(3):
	product = product * (count + 1)

	
>>> product
6
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
Enter the lower bound: 9
Enter the upper bound: 19
154
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
 Year    Starting balance  Interest Ending balance
    2             10000.0     500.0        10500.0
    3            10000.05  500.0025     10500.0525
    4             10000.1500.00500000000005      10500.105
    5            10000.15  500.0075     10500.1575
    6             10000.2500.0100000000000510500.210000000001
    7            10000.25500.01250000000005     10500.2625
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
 Year    Starting balance  Interest Ending balance
    2             10000.0     500.0        10500.0
    3            10000.05  500.0025     10500.0525
    4            10000.15  500.0075     10500.1575
    5             10000.3   500.01510500.314999999999
    6             10000.5500.02500000000003      10500.525
    7            10000.75  500.0375     10500.7875
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
 Year    Starting balance  Interest Ending balance
    2              1000.0      50.0         1050.0
    3             1050.05   52.5025      1102.5525
    4           1102.6525 55.1326251157.7851249999999
    5         1157.93512557.89675625  1215.83188125
    6       1216.0318812560.80159406251276.8334753125
    7     1277.083475312563.8541737656250061340.937649078125
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
 Year    Starting balance  Interest Ending balance
    2               10000       500          10500
    3               10500       525          11025
    4               11025       551          11576
    5               11576       579          12155
    6               12155       608          12763
    7               12763       638          13401
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
 Year    Starting balance       Interest      Ending balance
    2               10000       500          10500
    3               10500       525          11025
    4               11025       551          11576
    5               11576       579          12155
    6               12155       608          12763
    7               12763       638          13401
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
 Year    Starting balance       Interest      Ending balance
    2             10000.0          500.0             10500.0
    3            10500.05          525.0            11025.05
    4            11025.15         551.26            11576.41
    5            11576.56         578.83            12155.39
    6            12155.59         607.78            12763.37
    7            12763.62         638.18             13401.8
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
 Year    Starting balance       Interest      Ending balance
    1             10000.0          500.0             10500.0
    2            10500.05          525.0            11025.05
    3            11025.15         551.26            11576.41
    4            11576.56         578.83            12155.39
    5            12155.59         607.78            12763.37
    6            12763.62         638.18             13401.8
>>> import decimal
>>> help(decimal)

>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
 Year    Starting balance       Interest      Ending balance
    1             10000.0          500.0             10500.0
    2            10500.05          525.0            11025.05
    3            11025.15         551.26            11576.41
    4            11576.56         578.83            12155.39
    5            12155.59         607.78            12763.37
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
 Year    Starting balance       Interest      Ending balance
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Documents/20200326(newproj).py", line 128, in <module>
    startb = decimal((endb + count * intr), 2)
NameError: name 'decimal' is not defined
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
Enter the investment amount: 999
Enter the number of years: 5
Enter the rate as a %: 5
 Year    Starting balance       Interest      Ending balance
    1               999.0          49.95             1048.95
    2             1048.95        52.4475           1101.3975
    3           1101.3975      55.069875         1156.467375
    4         1156.467375    57.82336875       1214.29074375
    5       1214.29074375  60.7145371875     1275.0052809375
Ending balance: $ 1275.0052809375
Total interest earned: $ 276.0052809375
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
Enter the investment amount: 10000.00
Enter the number of years: 5
Enter the rate as a %: 5
 Year    Starting balance       Interest      Ending balance
    1             10000.0          500.0             10500.0
    2             10500.0          525.0             11025.0
    3             11025.0         551.25            11576.25
    4            11576.25       578.8125          12155.0625
    5          12155.0625     607.753125        12762.815625
Ending balance: $ 12762.82
Total interest earned: $ 2762.82
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
Enter the investment amount: 10000.00
Enter the number of years: 5
Enter the rate as a %: 5
 Year    Starting balance       Interest      Ending balance
    1             10000.0          500.0             10500.0
    2             10500.0          525.0             11025.0
    3             11025.0         551.25            11576.25
    4            11576.25         578.81            12155.06
    5            12155.06         607.75            12762.81
Ending balance: $ 12762.81
Total interest earned: $ 2762.81
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
Enter the investment amount: 10000.00
Enter the number of years: 5
Enter the rate as a %: 5
 Year    Starting balance       Interest      Ending balance
    1             10000.0          500.0             10500.0
    2             10500.0          525.0             11025.0
    3             11025.0         551.25            11576.25
    4            11576.25         578.81            12155.06
    5            12155.06         607.75            12762.81
Ending balance: $ 12762.81
Total interest earned: $ 2762.81
>>> member = ['hsiao ting', 'zheng hong', 'athena', 'kaijie']
>>> member
['hsiao ting', 'zheng hong', 'athena', 'kaijie']
>>> member.append('wei hong', 'taylor')
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    member.append('wei hong', 'taylor')
TypeError: append() takes exactly one argument (2 given)
>>> member.append('wei hong')
>>> member
['hsiao ting', 'zheng hong', 'athena', 'kaijie', 'wei hong']
>>> len(member)
5
>>> member.extend('taylor', 'liangce')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    member.extend('taylor', 'liangce')
TypeError: extend() takes exactly one argument (2 given)
>>> member.extend(['taylor', 'liangce'])
>>> member
['hsiao ting', 'zheng hong', 'athena', 'kaijie', 'wei hong', 'taylor', 'liangce']
>>> len(member)
7
>>> member.insert(1, )
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    member.insert(1, )
TypeError: insert expected 2 arguments, got 1
>>> member.insert(0, 'xinyi')
>>> member
['xinyi', 'hsiao ting', 'zheng hong', 'athena', 'kaijie', 'wei hong', 'taylor', 'liangce']
>>> member[0]
'xinyi'
>>> member[1]
'hsiao ting'
>>> temp = member[0]
>>> member[0] = member[1]
>>> member
['hsiao ting', 'hsiao ting', 'zheng hong', 'athena', 'kaijie', 'wei hong', 'taylor', 'liangce']
>>> member[1] = temp
>>> member
['hsiao ting', 'xinyi', 'zheng hong', 'athena', 'kaijie', 'wei hong', 'taylor', 'liangce']
>>> member.insert(7, 'sam')
>>> member
['hsiao ting', 'xinyi', 'zheng hong', 'athena', 'kaijie', 'wei hong', 'taylor', 'sam', 'liangce']
>>> member.remove('wei hong')
>>> member
['hsiao ting', 'xinyi', 'zheng hong', 'athena', 'kaijie', 'taylor', 'sam', 'liangce']
>>> member.remove('hsiaohong')
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    member.remove('hsiaohong')
ValueError: list.remove(x): x not in list
>>> member.del('sam')
SyntaxError: invalid syntax
>>> del member[1]
>>> member
['hsiao ting', 'zheng hong', 'athena', 'kaijie', 'taylor', 'sam', 'liangce']
>>> member.insert(5, 'xinyi')
>>> member
['hsiao ting', 'zheng hong', 'athena', 'kaijie', 'taylor', 'xinyi', 'sam', 'liangce']
>>> member.pop()
'liangce'
>>> member
['hsiao ting', 'zheng hong', 'athena', 'kaijie', 'taylor', 'xinyi', 'sam']
>>> member member.pop()
SyntaxError: invalid syntax
>>> name = member.pop()
>>> name
'sam'
>>> member.pop(1)
'zheng hong'
>>> member
['hsiao ting', 'athena', 'kaijie', 'taylor', 'xinyi']
>>> member.extend(['sam', 'liangce', 'zhenghong', 'wei hong'])
>>> member
['hsiao ting', 'athena', 'kaijie', 'taylor', 'xinyi', 'sam', 'liangce', 'zhenghong', 'wei hong']
>>> member.pop(1)
'athena'
>>> member.pop
<built-in method pop of list object at 0x10a07ef00>
>>> member
['hsiao ting', 'kaijie', 'taylor', 'xinyi', 'sam', 'liangce', 'zhenghong', 'wei hong']
>>> member.insert(1, 'zhenghong')
>>> member
['hsiao ting', 'zhenghong', 'kaijie', 'taylor', 'xinyi', 'sam', 'liangce', 'zhenghong', 'wei hong']
>>> del member [7]
>>> member
['hsiao ting', 'zhenghong', 'kaijie', 'taylor', 'xinyi', 'sam', 'liangce', 'wei hong']
>>> member[1:3]
['zhenghong', 'kaijie']
>>> member
['hsiao ting', 'zhenghong', 'kaijie', 'taylor', 'xinyi', 'sam', 'liangce', 'wei hong']
>>> len(member)
8
>>> member[1:9]
['zhenghong', 'kaijie', 'taylor', 'xinyi', 'sam', 'liangce', 'wei hong']
>>> member[0:9]
['hsiao ting', 'zhenghong', 'kaijie', 'taylor', 'xinyi', 'sam', 'liangce', 'wei hong']
>>> member[9]
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    member[9]
IndexError: list index out of range
>>> member[:9]
['hsiao ting', 'zhenghong', 'kaijie', 'taylor', 'xinyi', 'sam', 'liangce', 'wei hong']
>>> member[0:]
['hsiao ting', 'zhenghong', 'kaijie', 'taylor', 'xinyi', 'sam', 'liangce', 'wei hong']
>>> member[:]
['hsiao ting', 'zhenghong', 'kaijie', 'taylor', 'xinyi', 'sam', 'liangce', 'wei hong']
\
>>> member2 = member[:]
>>> member2
['hsiao ting', 'zhenghong', 'kaijie', 'taylor', 'xinyi', 'sam', 'liangce', 'wei hong']
>>> member
['hsiao ting', 'zhenghong', 'kaijie', 'taylor', 'xinyi', 'sam', 'liangce', 'wei hong']
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
Enter the investment amount: 10000.00
Enter the number of years: 5
Enter the rate as a %: 5
 Year    Starting balance       Interest      Ending balance
1.000000        10000.000000     500.000000        10500.000000
2.000000        10500.000000     525.000000        11025.000000
3.000000        11025.000000     551.250000        11576.250000
4.000000        11576.250000     578.810000        12155.060000
5.000000        12155.060000     607.750000        12762.810000
Ending balance: $ 12762.81
Total interest earned: $ 2762.81
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
Enter the investment amount: 10000.00
Enter the number of years: 5
Enter the rate as a %: 5
 Year    Starting balance       Interest      Ending balance
    1               10000            500               10500
    2               10500            525               11025
    3               11025            551               11576
    4               11576            578               12155
    5               12155            607               12762
Ending balance: $ 12762.81
Total interest earned: $ 2762.81
>>> round(1.65)
2
>>> round(1.49)
1
>>> round(1.5)
2
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
Enter the investment amount: 10000.00
Enter the number of years: 5
Enter the rate as a %: 5
 Year    Starting balance       Interest      Ending balance
    1            10000.00         500.00            10500.00
    2            10500.00         525.00            11025.00
    3            11025.00         551.25            11576.25
    4            11576.25         578.81            12155.06
    5            12155.06         607.75            12762.82
Ending balance: $ 12762.82
Total interest earned: $ 2762.82
>>> 
=================== RESTART: /Users/hsiaotingluv/Documents/20200326(newproj).py ===================
 Year    Starting balance       Interest      Ending balance
    1             10000.0          500.0             10500.0
    2            10500.05          525.0            11025.05
    3            11025.15         551.26            11576.41
    4            11576.56         578.83            12155.39
    5            12155.59         607.78            12763.37
>>> 