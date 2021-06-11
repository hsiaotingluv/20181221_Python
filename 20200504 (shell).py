Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ========
Enter a number and its base to convert to decimal, or 'quit' to quit: A,16
hello
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 106, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 101, in main
    print(hexToDecimal(num))
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 90, in hexToDecimal
    decNum += 16 ** power * numbersss(num)
TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: A,16
The converted number is 10
Enter a number and its base to convert to decimal, or 'quit' to quit: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: A,16
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 103, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 98, in main
    print(hexToDecimal(num))
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 87, in hexToDecimal
    decNum += 16 ** power * getNumbers(num)
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 79, in getNumbers
    print(dictionary[digit])
KeyError: 0
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: A,16
hello
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 104, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 99, in main
    print(hexToDecimal(num))
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 88, in hexToDecimal
    decNum += 16 ** power * getNumbers(num)
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 80, in getNumbers
    print(dictionary[digit])
KeyError: 0
>>> x = "A5"
>>> for digit in range(len(x)):
	print(dictionary[digit])

	
Traceback (most recent call last):
  File "<pyshell#3>", line 2, in <module>
    print(dictionary[digit])
NameError: name 'dictionary' is not defined
>>> dictionary = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, \
                  "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
>>> for digit in range(len(x)):
	print(dictionary[digit])

	
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    print(dictionary[digit])
KeyError: 0
>>> dictionary[1]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dictionary[1]
KeyError: 1
>>> for digit in range(len(x)):
	print(dictionary["digit"])

	
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    print(dictionary["digit"])
KeyError: 'digit'
>>> for digit in range(len(x)):
	print(digit)
	print(dictionary["digit"])

	
0
Traceback (most recent call last):
  File "<pyshell#11>", line 3, in <module>
    print(dictionary["digit"])
KeyError: 'digit'
>>> dictionary = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, \
                  "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
>>> 
>>> for digit in range(len(x)):
	print(dictionary[digit])

	
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    print(dictionary[digit])
KeyError: 0
>>> for digit in range(len(x)):
	print(digit)
	print(dictionary["digit"])

	
0
Traceback (most recent call last):
  File "<pyshell#17>", line 3, in <module>
    print(dictionary["digit"])
KeyError: 'digit'
>>> dictionary["0"]
0
>>> dictionary["A"]
10
>>> for digit in range(len(x)):
	print(digit)
	print(dictionary["digit"])

	
0
Traceback (most recent call last):
  File "<pyshell#21>", line 3, in <module>
    print(dictionary["digit"])
KeyError: 'digit'
>>> for digit in range(len(x)):
	print(digit)
	print(dictionary[digit])

	
0
Traceback (most recent call last):
  File "<pyshell#23>", line 3, in <module>
    print(dictionary[digit])
KeyError: 0
>>> for digit in range(len(x)):
	print(digit)
	print(dictionary[str(digit)])

	
0
0
1
1
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: A,16
0
The converted number is 0
Enter a number and its base to convert to decimal, or 'quit' to quit: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: A,16
10
The converted number is 10
Enter a number and its base to convert to decimal, or 'quit' to quit: A5,16
10
10
The converted number is 170
Enter a number and its base to convert to decimal, or 'quit' to quit: quit
>>> x = "A5"
>>> x[0]
'A'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: A5,16
The converted number is 90
Enter a number and its base to convert to decimal, or 'quit' to quit: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: A5,16
The converted number is 165
Enter a number and its base to convert to decimal, or 'quit' to quit: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: A,16
The converted number is 10
Enter a number and its base to convert to decimal, or 'quit' to quit: a,16
The converted number is 170
Enter a number and its base to convert to decimal, or 'quit' to quit: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: a,16
The converted number is 10
Enter a number and its base to convert to decimal, or 'quit' to quit: a5,16
The converted number is 697765
Enter a number and its base to convert to decimal, or 'quit' to quit: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: a5,16
A5
A5A5
A5A5
The converted number is 42405
Enter a number and its base to convert to decimal, or 'quit' to quit: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: a5,16
A
A5
A5
The converted number is 165
Enter a number and its base to convert to decimal, or 'quit' to quit: bb,16
A5B
A5BB
A5BB
The converted number is 42427
Enter a number and its base to convert to decimal, or 'quit' to quit: quit
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: bb,16
The converted number is 187
Enter a number and its base to convert to decimal, or 'quit' to quit: 1010,2
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 112, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 109, in main
    print(repToDecimal(num, base))
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 66, in repToDecimal
    num = int(num)
ValueError: invalid literal for int() with base 10: 'BB1010'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: 1010,2
The converted number is 10
Enter a number and its base to convert to decimal, or 'quit' to quit: bb,16
The converted number is 1052859
Enter a number and its base to convert to decimal, or 'quit' to quit: 1010,2
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 112, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 109, in main
    print(repToDecimal(num, base))
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 66, in repToDecimal
    num = int(num)
ValueError: invalid literal for int() with base 10: '1010BB1010'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: 1010,2
The converted number is 10
Enter a number and its base to convert to decimal, or 'quit' to quit: bb,16
The converted number is 187
Enter a number and its base to convert to decimal, or 'quit' to quit: 1010,2
The converted number is 10
Enter a number and its base to convert to decimal, or 'quit' to quit: 273,8
The converted number is 187
Enter a number and its base to convert to decimal, or 'quit' to quit: 10111011,2
The converted number is 187
Enter a number and its base to convert to decimal, or 'quit' to quit: a6f,16
The converted number is 2671
Enter a number and its base to convert to decimal, or 'quit' to quit: 5157,8
The converted number is 2671
Enter a number and its base to convert to decimal, or 'quit' to quit: 10100110111,2
The converted number is 1335
Enter a number and its base to convert to decimal, or 'quit' to quit: 1001, 2
The converted number is 9
Enter a number and its base to convert to decimal, or 'quit' to quit: quit
>>> x = "101, 2"
>>> x.remove(" ")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x.remove(" ")
AttributeError: 'str' object has no attribute 'remove'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter a number and its base to convert to decimal, or 'quit' to quit: 1001,2
The converted number is 9
Enter a number and its base to convert to decimal, or 'quit' to quit: 1001, 2
The converted number is 9
Enter a number and its base to convert to decimal, or 'quit' to quit: 1010,2
The converted number is 10
Enter a number and its base to convert to decimal, or 'quit' to quit: quit
>>> num = " 9"
>>> num = int(num)
>>> num
9
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter the file name to import: nouns.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')}
Enter the file name to import:  conjunctions
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 59, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 49, in main
    x = getWords(fileName)
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 7, in getWords
    f = open(fileName, "r")
FileNotFoundError: [Errno 2] No such file or directory: ' conjunctions'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter the file name to import: conjunctions
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 59, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 49, in main
    x = getWords(fileName)
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 7, in getWords
    f = open(fileName, "r")
FileNotFoundError: [Errno 2] No such file or directory: 'conjunctions'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter the file name to import: conjunctions.txt
{'conjunctions': ('AND', 'BUT', 'YET', 'UNTIL', 'IF', 'FOR')}
Enter the file name to import: nouns.txt
{'conjunctions': ('AND', 'BUT', 'YET', 'UNTIL', 'IF', 'FOR'), 'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')}
Enter the file name to import: verbs.txt
{'conjunctions': ('AND', 'BUT', 'YET', 'UNTIL', 'IF', 'FOR'), 'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')}
Enter the file name to import: prepositions.txt
{'conjunctions': ('AND', 'BUT', 'YET', 'UNTIL', 'IF', 'FOR'), 'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')}
Enter the file name to import: articles.txt
{'conjunctions': ('AND', 'BUT', 'YET', 'UNTIL', 'IF', 'FOR'), 'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER'), 'articles': ('A', 'AN', 'THE')}
Enter the file name to import: adjectives.txt
{'conjunctions': ('AND', 'BUT', 'YET', 'UNTIL', 'IF', 'FOR'), 'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER'), 'articles': ('A', 'AN', 'THE'), 'adjectives': ('HAPPY', 'HILARIOUS', 'FUNNY', 'INTERESTING', 'PAINFUL', 'BEAUTIFUL', 'PRETTY', 'COOL')}
Enter the number of sentences: 2
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 59, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 57, in main
    print(sentence(dictionary))
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 17, in sentence
    return nounPhrase(dictionary) + " " + verbPhrase(dictionary) + \
  File "/Users/hsiaotingluv/Desktop/python/20200503 (file).py", line 33, in verbPhrase
    if probablitiy == 1:
NameError: name 'probablitiy' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter the file name to import: articles.txt
Enter the file name to import: nouns.txt
Enter the file name to import: adjectives.txt
Enter the file name to import: verbs.txt
Enter the file name to import: prepositions.txt
Enter the file name to import: conjunctions.txt
Enter the number of sentences: 3
AN SAM STOOD THE HAPPY BROTHERYETA FUNNY BAT RAN AN HSIAOTING
A HAPPY BAT LIKED A HAPPY BROTHER
THE SAM PLAYED AN FUNNY SAM ABOUT AN PRETTY FANFORAN CAT LIKED THE BOY
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter the file name to import: conjunctions.txt
Enter the file name to import: nouns.txt
Enter the file name to import: verbs.txt
Enter the file name to import: adjectives.txt
Enter the file name to import: prepositions.txt
Enter the file name to import: articles.txt
Enter the number of sentences: 4
A INTERESTING XINYI SMELL A PAINFUL XINYI
THE DAD SANG THE ZHENGHONG FOR THE HSIAOTING
THE BAT STOOD THE FUNNY BAT ABOUT A SISTERYET A MOM STOOD A FUNNY XINYI
A HSIAOTING WALKED THE BOY ABOUT A MOMIF THE BEAUTIFUL GIRL CLAPPED A BALL FOR A DOG
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter the file name to import: conjunctions.txt
Enter the file name to import: nouns.txt
Enter the file name to import: verbs.txt
Enter the file name to import: adjectives.txt
Enter the file name to import: prepositions.txt
Enter the file name to import: articles.txt
Enter the number of sentences: 5
A COOL CAT SMELLS A PRETTY GIRL FROM THE PRETTY CUP
A PHONE SMELLS THE CUP INTO A FUNNY GIRL
THE HILARIOUS MOM LIKED A HAPPY CUPAND A DAD SAW A COOL CUP
THE GIRL SANG THE HILARIOUS CAT BENEATH THE BATYET A BAT HEARD A DAD
THE PAINFUL SISTER LIKED A HAPPY CUP ONTO THE COOL SISTER
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200503 (file).py ===========
Enter the file name to import: conjunctions.txt
Enter the file name to import: nouns.txt
Enter the file name to import: verbs.txt
Enter the file name to import: adjectives.txt
Enter the file name to import: prepositions.txt
Enter the file name to import: articles.txt
Enter the number of sentences: 5
THE BOY STOOD A SISTER
A PRETTY CAT LIKED THE CUP BUT THE DOG SAW A PHONE UNDER THE MOM
THE DOG HITS THE FUNNY DOG IF THE BEAUTIFUL GIRL TALKED A HILARIOUS BOY BELOW THE COOL BALL
A HILARIOUS MOM HEARD A BOY OF THE BROTHER
A PAINFUL CAT HEARD A FUNNY BALL IN A PRETTY BAT IF THE CAT HITS A PAINFUL PHONE ALONG A CUP
>>> 13 % 16
13
>>> 13 / 16
0.8125
>>> dictionary = {"hello", 5}
>>> dictionary
{'hello', 5}
>>> dictionary[5]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    dictionary[5]
TypeError: 'set' object is not subscriptable
>>> dictionary["hello"]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    dictionary["hello"]
TypeError: 'set' object is not subscriptable
>>> dictionary.keys()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    dictionary.keys()
AttributeError: 'set' object has no attribute 'keys'
>>> dictionary.keys(5)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    dictionary.keys(5)
AttributeError: 'set' object has no attribute 'keys'
>>> dictionary
{'hello', 5}
>>> dictionary["world"] = 10
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    dictionary["world"] = 10
TypeError: 'set' object does not support item assignment
>>> dictionary["world"] = "10"
Traceback (most recent call last):

  File "<pyshell#43>", line 1, in <module>
    dictionary["world"] = "10"
TypeError: 'set' object does not support item assignment
>>> dict["hello":1]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dict["hello":1]
TypeError: 'type' object is not subscriptable
>>> dict["hello"] = 1
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    dict["hello"] = 1
TypeError: 'type' object does not support item assignment
>>> dictionary = {}
>>> dictionary["hello"] = 10
>>> dictionary["world"] = 5
>>> dictionary.values()
dict_values([10, 5])
>>> dictionary.values(1)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dictionary.values(1)
TypeError: values() takes no arguments (1 given)
>>> dictionary.values(10)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    dictionary.values(10)
TypeError: values() takes no arguments (1 given)
>>> dictionary.values[10]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dictionary.values[10]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> dictionary.items()
dict_items([('hello', 10), ('world', 5)])
>>> dictionary.index(10)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    dictionary.index(10)
AttributeError: 'dict' object has no attribute 'index'
>>> dictionary[10]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    dictionary[10]
KeyError: 10
>>> dictionary["hello"]
10
>>> dictionary.get[10]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    dictionary.get[10]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> dictionary.get(10)
>>> dictionary
{'hello': 10, 'world': 5}
>>> dictionary.get(10)
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number: 317547,16
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 48, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 44, in main
    print(decimalToHex(decimal, base))
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 22, in decimalToHex
    while a > 1:
UnboundLocalError: local variable 'a' referenced before assignment
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number: 317547,16
The number in 16 base is: 04
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number: 317547,16
5
0
04
The number in 16 base is: 04
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number: 317547,16
5
4
The number in 16 base is: 4
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number: 317547,16
i is 4
hex is 4
4
i is 3
hex is 77
i is 2
hex is 1240
i is 1
hex is 19846
The number in 16 base is: 4
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number: 317547,16
i is 4
hex is 4
4
317547
i is 3
hex is 77
317547
i is 2
hex is 1240
317547
i is 1
hex is 19846
317547
The number in 16 base is: 4
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number: 317547,16
i is 4
hex is 4
4
55403
i is 3
hex is 13
4D
2155
i is 2
hex is 8
4D8
107
i is 1
hex is 6
4D86
11
The number in 16 base is: 4D86
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number: 317547,16
i is 4
hex is 4
4
55403
i is 3
hex is 13
4D
2155
i is 2
hex is 8
4D8
107
i is 1
hex is 6
4D86
11
i is 0
hex is 11
4D86B
0
The number in 16 base is: 4D86B
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number: 13,8
The number in 8 base is: 15
>>> 13,2
(13, 2)
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 55, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 40, in main
    x = input("Enter a decimal integer and the base of the converted number", \
TypeError: input expected at most 1 argument, got 2
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number or 'quit' to quit: 13,2
The number in 2 base is: 1101
Enter a decimal integer and the base of the converted number or 'quit' to quit: quit
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number or 'quit' to quit: D,16
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 55, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 46, in main
    decimal = int(decimal)
ValueError: invalid literal for int() with base 10: 'D'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number or 'quit' to quit: 13,16
D
The number in base 16 is: D
Enter a decimal integer and the base of the converted number or 'quit' to quit: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number or 'quit' to quit: 130,2
The number in base2 is: 10000010
Enter a decimal integer and the base of the converted number or 'quit' to quit: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter a decimal integer and the base of the converted number or 'quit' to quit: 130,2
The number in base 2 is: 10000010
Enter a decimal integer and the base of the converted number or 'quit' to quit: 130,8
The number in base 8 is: 202
Enter a decimal integer and the base of the converted number or 'quit' to quit: 130,9
The number in base 9 is: 154
Enter a decimal integer and the base of the converted number or 'quit' to quit: 130,16
The number in base 16 is: 82
Enter a decimal integer and the base of the converted number or 'quit' to quit: quit
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: 
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 59, in <module>
    fileName = input("Enter the name of a text file: ")
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
<built-in method sort of list object at 0x1021b2cc0>
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
None
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
None
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
Bae, hello.
My name is hsiaoting.
Hello world!
How are you?
Im fine!

['Bae,', 'hello.', 'My', 'name', 'is', 'hsiaoting.', 'Hello', 'world!', 'How', 'are', 'you?', 'Im', 'fine!']
None
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
['Bae,', 'hello.', 'My', 'name', 'is', 'hsiaoting.', 'Hello', 'world!', 'How', 'are', 'you?', 'Im', 'fine!']
>>> x = ['Bae,', 'hello.', 'My', 'name', 'is', 'hsiaoting.', 'Hello', 'world!', 'How', 'are', 'you?', 'Im', 'fine!']
>>> x
['Bae,', 'hello.', 'My', 'name', 'is', 'hsiaoting.', 'Hello', 'world!', 'How', 'are', 'you?', 'Im', 'fine!']
>>> x.sort()
>>> x
['Bae,', 'Hello', 'How', 'Im', 'My', 'are', 'fine!', 'hello.', 'hsiaoting.', 'is', 'name', 'world!', 'you?']
>>> text = sorted(x, key = str.lower)
>>> text
['are', 'Bae,', 'fine!', 'Hello', 'hello.', 'How', 'hsiaoting.', 'Im', 'is', 'My', 'name', 'world!', 'you?']
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
['are', 'Bae,', 'fine!', 'Hello', 'hello.', 'How', 'hsiaoting.', 'Im', 'is', 'My', 'name', 'world!', 'you?']
>>> dictionary = {"hello":2}
>>> dictionary.get(2)
>>> dictionary
{'hello': 2}
>>> dictionary.get("hello")
2
>>> dictionary.items()
dict_items([('hello', 2)])
>>> dictionary["world":3]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    dictionary["world":3]
TypeError: unhashable type: 'slice'
>>> dictionary["world"] = 3
>>> dictionary.keys()
dict_keys(['hello', 'world'])
>>> dictionary.values()
dict_values([2, 3])
>>> dictionary.keys().split
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    dictionary.keys().split
AttributeError: 'dict_keys' object has no attribute 'split'
>>> dictionary.keys().split()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    dictionary.keys().split()
AttributeError: 'dict_keys' object has no attribute 'split'
>>> dictionary.items()
dict_items([('hello', 2), ('world', 3)])
>>> words = ["hello", "world"]
>>> words[1]
'world'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
     words         frequencies
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 93, in <module>
    print("%10s%20s" % (words[i], frequencies[i]))
TypeError: 'dict_keys' object is not subscriptable
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
     words         frequencies
         0                   1
         1                   1
         2                   1
         3                   1
         4                   1
         5                   1
         6                   1
         7                   1
         8                   1
         9                   1
        10                   1
        11                   1
        12                   1
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
['are', 'Bae,', 'fine!', 'Hello', 'hello.', 'How', 'hsiaoting.', 'Im', 'is', 'My', 'name', 'world!', 'you?']
     words         frequencies
0
{0: 1}
1
{0: 1, 1: 1}
2
{0: 1, 1: 1, 2: 1}
3
{0: 1, 1: 1, 2: 1, 3: 1}
4
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
5
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
6
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
7
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}
8
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}
9
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
10
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1}
11
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1}
12
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1}
         0                   1
         1                   1
         2                   1
         3                   1
         4                   1
         5                   1
         6                   1
         7                   1
         8                   1
         9                   1
        10                   1
        11                   1
        12                   1
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
     words         frequencies
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 80, in <module>
    for word in wordList():
TypeError: 'list' object is not callable
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
     words         frequencies
are
{'are': 1}
Bae,
{'are': 1, 'Bae,': 1}
fine!
{'are': 1, 'Bae,': 1, 'fine!': 1}
Hello
{'are': 1, 'Bae,': 1, 'fine!': 1, 'Hello': 1}
hello.
{'are': 1, 'Bae,': 1, 'fine!': 1, 'Hello': 1, 'hello.': 1}
How
{'are': 1, 'Bae,': 1, 'fine!': 1, 'Hello': 1, 'hello.': 1, 'How': 1}
hsiaoting.
{'are': 1, 'Bae,': 1, 'fine!': 1, 'Hello': 1, 'hello.': 1, 'How': 1, 'hsiaoting.': 1}
Im
{'are': 1, 'Bae,': 1, 'fine!': 1, 'Hello': 1, 'hello.': 1, 'How': 1, 'hsiaoting.': 1, 'Im': 1}
is
{'are': 1, 'Bae,': 1, 'fine!': 1, 'Hello': 1, 'hello.': 1, 'How': 1, 'hsiaoting.': 1, 'Im': 1, 'is': 1}
My
{'are': 1, 'Bae,': 1, 'fine!': 1, 'Hello': 1, 'hello.': 1, 'How': 1, 'hsiaoting.': 1, 'Im': 1, 'is': 1, 'My': 1}
name
{'are': 1, 'Bae,': 1, 'fine!': 1, 'Hello': 1, 'hello.': 1, 'How': 1, 'hsiaoting.': 1, 'Im': 1, 'is': 1, 'My': 1, 'name': 1}
world!
{'are': 1, 'Bae,': 1, 'fine!': 1, 'Hello': 1, 'hello.': 1, 'How': 1, 'hsiaoting.': 1, 'Im': 1, 'is': 1, 'My': 1, 'name': 1, 'world!': 1}
you?
{'are': 1, 'Bae,': 1, 'fine!': 1, 'Hello': 1, 'hello.': 1, 'How': 1, 'hsiaoting.': 1, 'Im': 1, 'is': 1, 'My': 1, 'name': 1, 'world!': 1, 'you?': 1}
       are                   1
      Bae,                   1
     fine!                   1
     Hello                   1
    hello.                   1
       How                   1
hsiaoting.                   1
        Im                   1
        is                   1
        My                   1
      name                   1
    world!                   1
      you?                   1
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: 
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 72, in <module>
    fileName = input("Enter the name of a text file: ")
KeyboardInterrupt
>>> list
<class 'list'>
>>> words
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    words
NameError: name 'words' is not defined
>>> wordList
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    wordList
NameError: name 'wordList' is not defined
>>> wordList = ['Bae,', 'Hello', 'How', 'Im', 'My', 'are', 'fine!', 'hello.', 'hsiaoting.', 'is', 'name', 'world!', 'you?']
>>> wordList.lower()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    wordList.lower()
AttributeError: 'list' object has no attribute 'lower'
>>> x
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> wordList
['Bae,', 'Hello', 'How', 'Im', 'My', 'are', 'fine!', 'hello.', 'hsiaoting.', 'is', 'name', 'world!', 'you?']
>>> for i in range(len(wordList)):
	    wordList[i] = wordList[i].lower()

	    
>>> wordList
['bae,', 'hello', 'how', 'im', 'my', 'are', 'fine!', 'hello.', 'hsiaoting.', 'is', 'name', 'world!', 'you?']
>>> worldList.sort()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    worldList.sort()
NameError: name 'worldList' is not defined
>>> wordList.sort()
>>> wordList
['are', 'bae,', 'fine!', 'hello', 'hello.', 'how', 'hsiaoting.', 'im', 'is', 'my', 'name', 'world!', 'you?']
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
     words         frequencies
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 93, in <module>
    for word in wordList:
TypeError: 'NoneType' object is not iterable
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
['Bae', 'hello', 'My', 'name', 'is', 'hsiaoting', 'hello', 'world', 'How', 'are', 'you', 'Im', 'fine']
None
     words         frequencies
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 95, in <module>
    for word in wordList:
TypeError: 'NoneType' object is not iterable
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
bae, hello.
my name is hsiaoting.
hello world!
how are you?
im fine!

['bae', 'hello', 'my', 'name', 'is', 'hsiaoting', 'hello', 'world', 'how', 'are', 'you', 'im', 'fine']
None
     words         frequencies
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 93, in <module>
    for word in wordList:
TypeError: 'NoneType' object is not iterable
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 82, in <module>
    wordList = new_s.split().sorted()
AttributeError: 'list' object has no attribute 'sorted'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
None
     words         frequencies
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 90, in <module>
    for word in wordList:
TypeError: 'NoneType' object is not iterable
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
['bae', 'hello', 'my', 'name', 'is', 'hsiaoting', 'hello', 'world', 'how', 'are', 'you', 'im', 'fine']
['are', 'bae', 'fine', 'hello', 'hello', 'how', 'hsiaoting', 'im', 'is', 'my', 'name', 'world', 'you']
     words         frequencies
       are                   1
       bae                   1
      fine                   1
     hello                   1
       how                   1
 hsiaoting                   1
        im                   1
        is                   1
        my                   1
      name                   1
     world                   1
       you                   1
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200504 (file).py", line 103, in <module>
    print("%10s%20s" % (words[i], frequencies[i]))
IndexError: list index out of range
>>> dictionary
{'are': 1, 'bae': 1, 'fine': 1, 'hello': 1, 'how': 1, 'hsiaoting': 1, 'im': 1, 'is': 1, 'my': 1, 'name': 1, 'world': 1, 'you': 1}
>>> dictionary.get('hello')
1
>>> words
['are', 'bae', 'fine', 'hello', 'how', 'hsiaoting', 'im', 'is', 'my', 'name', 'world', 'you']
>>> words[0]
'are'
>>> wordList
['are', 'bae', 'fine', 'hello', 'hello', 'how', 'hsiaoting', 'im', 'is', 'my', 'name', 'world', 'you']
>>> len(wordList)
13
>>> words[12]
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    words[12]
IndexError: list index out of range
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200504 (file).py ===========
Enter the name of a text file: test1.txt
     words         frequencies
       are                   1
       bae                   1
      fine                   1
     hello                   2
       how                   1
 hsiaoting                   1
        im                   1
        is                   1
        my                   1
      name                   1
     world                   1
       you                   1
>>> 