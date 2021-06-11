Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> for x in range(1,10):
	print(x, end = " ")

	
1 2 3 4 5 6 7 8 9 
>>> for x in range(1,10):
	print(x, end = " ")
	print("dljfaskd")

	
1 dljfaskd
2 dljfaskd
3 dljfaskd
4 dljfaskd
5 dljfaskd
6 dljfaskd
7 dljfaskd
8 dljfaskd
9 dljfaskd
>>> for x in range(1,10):
	print(x, end = ". ")
	print("dljfaskd")

	
1. dljfaskd
2. dljfaskd
3. dljfaskd
4. dljfaskd
5. dljfaskd
6. dljfaskd
7. dljfaskd
8. dljfaskd
9. dljfaskd
>>> import random
>>> array = []
>>> for i in range(10):
	word = ""
	for j in range(10):
		num = random.randint(65,90)
		char = chr(num)
		word += char
	array.append(word)
print(array)
SyntaxError: invalid syntax
>>> for i in range(10):
	word = ""
	for j in range(10):
		num = random.randint(65,90)
		char = chr(num)
		word += char
	array.append(word)

	
>>> array
['ZQRHLLLSTM', 'XOCDKFEZGP', 'QURGYLRWMJ', 'LTREAUHZLK', 'SYFTUMVQZB', 'JLSOLAEJHG', 'MJMZUIYACD', 'PXPBQASZGX', 'NMAXVHQOYF', 'VNADFLLTKI']
>>> for x in range(1,10):
	print(x, end = ". ")
	print(array[x-1])

	
1. ZQRHLLLSTM
2. XOCDKFEZGP
3. QURGYLRWMJ
4. LTREAUHZLK
5. SYFTUMVQZB
6. JLSOLAEJHG
7. MJMZUIYACD
8. PXPBQASZGX
9. NMAXVHQOYF
>>> for x in range(10):
	print(x+1, end = ". ")
	print(array[x])

	
1. ZQRHLLLSTM
2. XOCDKFEZGP
3. QURGYLRWMJ
4. LTREAUHZLK
5. SYFTUMVQZB
6. JLSOLAEJHG
7. MJMZUIYACD
8. PXPBQASZGX
9. NMAXVHQOYF
10. VNADFLLTKI
>>> for item in array:
	print(item)

	
ZQRHLLLSTM
XOCDKFEZGP
QURGYLRWMJ
LTREAUHZLK
SYFTUMVQZB
JLSOLAEJHG
MJMZUIYACD
PXPBQASZGX
NMAXVHQOYF
VNADFLLTKI
>>> var = True
>>> done = True
>>> var = 10
>>> while not done:
	print("hello")
	if var == 10:
		done = False
	var += 1

	
>>> 
>>> done
True
>>> done = False
>>> while not done:
	print("hello")
	if var == 10:
		done = True
	var += 1

	
hello
>>> var = 0
>>> while not done:
	print("hello")
	if var == 10:
		done = True
	var += 1

	
>>> done = False
>>> while not done:
	print("hello")
	if var == 10:
		done = True
	var += 1

	
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
>>> 