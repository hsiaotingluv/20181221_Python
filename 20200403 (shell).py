Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = "Hsiao Ting"
>>> name[-1]
'g'
>>> name[3]
'a'
>>> len.name
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    len.name
AttributeError: 'builtin_function_or_method' object has no attribute 'name'
>>> len(name)
10
>>> for index in range(len(name))L
SyntaxError: invalid syntax
>>> for index in range(len(name)):
	print(index, name(index))

	
Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    print(index, name(index))
TypeError: 'str' object is not callable
>>> name(index)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    name(index)
TypeError: 'str' object is not callable
>>> for index in range(len(name)):
	    print(index, name[index])

	    
0 H
1 s
2 i
3 a
4 o
5  
6 T
7 i
8 n
9 g
>>> Namelist = ["HsiaoTing", "HsiaoTong", "HsiaoHong", "Hsiao"]
>>> for Name in Namelist:
	if "Hsiao" in Namelist:
		print(Name)

		
HsiaoTing
HsiaoTong
HsiaoHong
Hsiao
>>> strDummy = "Hello World, I am Hsiao Ting!"
>>> strDummy.split( )
['Hello', 'World,', 'I', 'am', 'Hsiao', 'Ting!']
>>> strDummy.replace("e", "s")
'Hsllo World, I am Hsiao Ting!'
>>> strDummy.lower()
'hello world, i am hsiao ting!'
>>> strDummy.higher()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    strDummy.higher()
AttributeError: 'str' object has no attribute 'higher'
>>> strDummy.upper()
'HELLO WORLD, I AM HSIAO TING!'
>>> strDummy.split(" ", 2)
['Hello', 'World,', 'I am Hsiao Ting!']
>>> strDummy.split(" ",2)
['Hello', 'World,', 'I am Hsiao Ting!']
>>> listDummy = ["Hello", "there", "ladies", "and", "gentlemen"]
>>> print(listDummy)
['Hello', 'there', 'ladies', 'and', 'gentlemen']
>>> " ".join(listDummy)
'Hello there ladies and gentlemen'
>>> strDummy.join(listDummy)
'HelloHello World, I am Hsiao Ting!thereHello World, I am Hsiao Ting!ladiesHello World, I am Hsiao Ting!andHello World, I am Hsiao Ting!gentlemen'
>>> " - ".join(listDummy)
'Hello - there - ladies - and - gentlemen'
>>> str.split(strDummy)
['Hello', 'World,', 'I', 'am', 'Hsiao', 'Ting!']
>>> str.upper(strDummy)
'HELLO WORLD, I AM HSIAO TING!'
>>> help(str)

>>> strDummy.strip()
'Hello World, I am Hsiao Ting!'
>>> strDummy.strip( )
'Hello World, I am Hsiao Ting!'
>>> strDummy.strip(" ")
'Hello World, I am Hsiao Ting!'
>>> strDummy.count("i")
2
>>> strDummy.capitalize()
'Hello world, i am hsiao ting!'
>>> strDummy.count(" ")
5
>>> strDummy.find("a")
15
>>> strDummy.find('l')
2
>>> strDummy.find("q")
-1
>>> strDummy.find("A")
-1
>>> strDummy.rfind("l")
9
>>> strDummy.rfind("a")
21
>>> strDummy.rfind("l")
9
>>> strDummy.lstrip()
'Hello World, I am Hsiao Ting!'
>>> strDummy.split(char)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    strDummy.split(char)
NameError: name 'char' is not defined
>>> strDummy.center(11)
'Hello World, I am Hsiao Ting!'
>>> strDummy.center(20)
'Hello World, I am Hsiao Ting!'
>>> strDummy.lens
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    strDummy.lens
AttributeError: 'str' object has no attribute 'lens'
>>> strDummy.join(hi)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    strDummy.join(hi)
NameError: name 'hi' is not defined
>>> strDummy.join("hi")
'hHello World, I am Hsiao Ting!i'
>>> strDummy.split(" ")
['Hello', 'World,', 'I', 'am', 'Hsiao', 'Ting!']
>>> sentence = "This sentence has no long words."
>>> print("There are", len(sentence), "words.")
There are 32 words.
>>> list = sentence.split()
>>> list
['This', 'sentence', 'has', 'no', 'long', 'words.']
>>> print("There are", len(list), "words")
There are 6 words
>>> sum = 0
>>> for word in list:
	sum += len(word)

	
>>> print("The average word length is", sum / len(list))
The average word length is 4.5
>>> len(word)
6
>>> word
'words.'
>>> open('20200329(test).txt')
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    open('20200329(test).txt')
FileNotFoundError: [Errno 2] No such file or directory: '20200329(test).txt'
>>> open('test.txt','r')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    open('test.txt','r')
FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
>>> 
===================== RESTART: /Users/hsiaotingluv/Documents/20200403(file).py ====================
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Documents/20200403(file).py", line 74, in <module>
    number = random.randiant(1, 500)
AttributeError: module 'random' has no attribute 'randiant'
>>> 
===================== RESTART: /Users/hsiaotingluv/Documents/20200403(file).py ====================
>>> 
===================== RESTART: /Users/hsiaotingluv/Documents/20200403(file).py ====================
>>> f = 10 20
SyntaxError: invalid syntax
>>> f = 10 20
SyntaxError: invalid syntax
>>> f = "abc eoifee", "\n", "esonf"
>>> f
('abc eoifee', '\n', 'esonf')
>>> f = "diojeofjwi fiwaoif aifjo "
>>> df
SyntaxError: invalid syntax
>>> f
'diojeofjwi fiwaoif aifjo '
>>> f.split()
['diojeofjwi', 'fiwaoif', 'aifjo']
>>> f = hi, i am hsaio ting! hi? are you there? i said: i am hsiao ting!
SyntaxError: invalid syntax
>>> f = "hi, i am hsaio ting! hi? are you there? i said: i am hsiao ting!"
>>> f.split(",", "!", "?", ":")
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    f.split(",", "!", "?", ":")
TypeError: split() takes at most 2 arguments (4 given)
>>> f.split(",", "!")
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    f.split(",", "!")
TypeError: 'str' object cannot be interpreted as an integer
>>> f.split(",")
['hi', ' i am hsaio ting! hi? are you there? i said: i am hsiao ting!']
>>> file = "hello"
>>> file.split()
['hello']
>>> 
===================== RESTART: /Users/hsiaotingluv/Documents/20200403(file).py ====================
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Documents/20200403(file).py", line 148, in <module>
    file = open("20200329(test).txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: '20200329(test).txt'
>>> 
===================== RESTART: /Users/hsiaotingluv/Documents/20200403(file).py ====================
>>> 
================== RESTART: /Users/hsiaotingluv/Desktop/python/20200402(file).py ==================
100:1	2	4	5	10	20	25	50	100	
sum of divisors is 0
101:1	101	
sum of divisors is 0
102:1	2	3	6	17	34	51	102	
sum of divisors is 0
103:1	103	
sum of divisors is 0
104:1	2	4	8	13	26	52	104	
sum of divisors is 0
105:1	3	5	7	15	21	35	105	
sum of divisors is 0
106:1	2	53	106	
sum of divisors is 0
107:1	107	
sum of divisors is 0
108:1	2	3	4	6	9	12	18	27	36	54	108	
sum of divisors is 0
109:1	109	
sum of divisors is 0
110:1	2	5	10	11	22	55	110	
sum of divisors is 0
110 has maximum sum of divisors.
Enter y to continue, n to stop: 
================== RESTART: /Users/hsiaotingluv/Desktop/python/20200402(file).py ==================
100:1	2	4	5	10	20	25	50	100	
sum of divisors is 217

101:1	101	
sum of divisors is 319

102:1	2	3	6	17	34	51	102	
sum of divisors is 535

103:1	103	
sum of divisors is 639

104:1	2	4	8	13	26	52	104	
sum of divisors is 849

105:1	3	5	7	15	21	35	105	
sum of divisors is 1041

106:1	2	53	106	
sum of divisors is 1203

107:1	107	
sum of divisors is 1311

108:1	2	3	4	6	9	12	18	27	36	54	108	
sum of divisors is 1591

109:1	109	
sum of divisors is 1701

110:1	2	5	10	11	22	55	110	
sum of divisors is 1917

110 has maximum sum of divisors.
Enter y to continue, n to stop: 
================== RESTART: /Users/hsiaotingluv/Desktop/python/20200402(file).py ==================
100: 1 2 4 5 10 20 25 50 100 
sum of divisors is 217

101: 1 101 
sum of divisors is 319

102: 1 2 3 6 17 34 51 102 
sum of divisors is 535

103: 1 103 
sum of divisors is 639

104: 1 2 4 8 13 26 52 104 
sum of divisors is 849

105: 1 3 5 7 15 21 35 105 
sum of divisors is 1041

106: 1 2 53 106 
sum of divisors is 1203

107: 1 107 
sum of divisors is 1311

108: 1 2 3 4 6 9 12 18 27 36 54 108 
sum of divisors is 1591

109: 1 109 
sum of divisors is 1701

110: 1 2 5 10 11 22 55 110 
sum of divisors is 1917

110 has maximum sum of divisors.
Enter y to continue, n to stop: 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200402(file).py ===========
Enter y to continue, n to stop: y
Enter the score: -1
Invalid number! Enter a number between 0 to 100!
Enter the score: 12
Failed
Enter the score: 1000
Invalid number! Enter a number between 0 to 100!
Enter the score: 30
Failed
Enter the score: 900
Invalid number! Enter a number between 0 to 100!
Enter the score: 90
Passed
Your average score is 44
Enter y to continue, n to stop: -1
Number of students passed is 0
Number of students with average of at least 80 is 0
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200402(file).py ===========
Enter y to continue, n to stop: y
Enter the score: -1
Invalid number! Enter a number between 0 to 100!
Enter the score: -1
Invalid number! Enter a number between 0 to 100!
Enter the score: -1
Invalid number! Enter a number between 0 to 100!
Enter the score: -1
Invalid number! Enter a number between 0 to 100!
Enter the score: 03
Failed
Enter the score: 10
Failed
Enter the score: 10
Failed
Your average score is 8
Enter y to continue, n to stop: n
Number of students passed is 0
Number of students with average of at least 80 is 0
>>> 