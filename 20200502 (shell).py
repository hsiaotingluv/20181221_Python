Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5 % 2
1
>>> list = [1, 5, 35, 43, 3]
>>> list.sort()
>>> list
[1, 3, 5, 35, 43]
>>> 5 / 2
2.5
>>> int(5 / 2)
2
>>> list.get(2)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list.get(2)
AttributeError: 'list' object has no attribute 'get'
>>> list.index(2)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    list.index(2)
ValueError: 2 is not in list
>>> list.index()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    list.index()
TypeError: index expected at least 1 argument, got 0
>>> list.index(5, 1)
2
>>> list.find(5)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    list.find(5)
AttributeError: 'list' object has no attribute 'find'
>>> list[5]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    list[5]
IndexError: list index out of range
>>> list[2]
5
>>> list = [1, 5, 35, 43, 3, 4]
>>> list.sort()
>>> list
[1, 3, 4, 5, 35, 43]
>>> list.count("5")
0
>>> list.count(5)
1
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers: 12, 33, 23, 41, 24, 42
Compute median / mode / mean: median
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 66, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 56, in main
    print(median(sentence))
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 16, in median
    median = (list[num] + list[num + 1]) / 2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers: 12 33 42 41 11
Compute median / mode / mean: median
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 67, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 57, in main
    print(median(sentence))
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 6, in median
    for word in sentence.split(""):
ValueError: empty separator
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers: 
	12 33 42 41 11
Compute median / mode / mean: Please enter a value mode.
Compute median / mode / mean: median
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers: 12 33 42 41 11
Compute median / mode / mean: median
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 69, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 59, in main
    print(median(sentence))
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 19, in median
    return "The median is " + median
TypeError: can only concatenate str (not "int") to str
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers: 
	12 33 42 41 11
Compute median / mode / mean: Please enter a value mode.
Compute median / mode / mean: median
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 69, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 59, in main
    print(median(sentence))
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 17, in median
    median = (list[num] + list[num + 1]) / 2
IndexError: list index out of range
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers: 12 33 42 41 11
Compute median / mode / mean: median
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33
The median is 33Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 69, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 59, in main
    print(median(sentence))
KeyboardInterrupt
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers: 12 33 42 41 11
Compute median / mode / mean: median
The median is 33
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers or 'quit' to quit: 12 33 42 41 11
Compute median / mode / mean: mode
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 72, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 62, in main
    print(mode(sentence))
TypeError: 'str' object is not callable
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers or 'quit' to quit: 12 33 42 41 11
Compute median / mode / mean: mode
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 73, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 63, in main
    print(mode(sentence))
TypeError: 'str' object is not callable
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers or 'quit' to quit: 12 33 42 41 11
Compute median / mode / mean: mean
The mean is 27.8
Enter a set of numbers or 'quit' to quit: j
The mean is 27.8
Enter a set of numbers or 'quit' to quit: j
The mean is 27.8
Enter a set of numbers or 'quit' to quit: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers or 'quit' to quit: 12 33 42 41 11
Compute median / mode / mean: mean
The mean is 27.8
Enter a set of numbers or 'quit' to quit: j
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 73, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 66, in main
    print(mean(sentence))
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 48, in mean
    num = int(word)
ValueError: invalid literal for int() with base 10: 'j'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers or 'quit' to quit: 12 33 42 41 11
Compute median / mode / mean: mean
The mean is 27.8
Enter a set of numbers or 'quit' to quit: 12 33 42 41 11
The mean is 27.8
Enter a set of numbers or 'quit' to quit: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers or 'quit' to quit: 12 33 42 41 11
Compute median / mode / mean: mean
The mean is 27.8
Enter a set of numbers or 'quit' to quit: 12 33 42 41 11
Compute median / mode / mean: j
Please enter a valid mode.
Compute median / mode / mean: j
Please enter a valid mode.
Compute median / mode / mean: median
The median is 33
Enter a set of numbers or 'quit' to quit: quit
Compute median / mode / mean: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers or 'quit' to quit: quit
Compute median / mode / mean: d
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers or 'quit' to quit: 111 31 3
Compute median / mode / mean: median
The median is 31
Enter a set of numbers or 'quit' to quit: 24 42
Compute median / mode / mean:  meean
Please enter a valid mode.
Compute median / mode / mean: mean
Enter a set of numbers or 'quit' to quit: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers or 'quit' to quit: 82 83
Compute median / mode / mean: mean
The mean is 82.5
Enter a set of numbers or 'quit' to quit: d
Compute median / mode / mean: mean
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 79, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 67, in main
    print(mean(sentence))
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 48, in mean
    num = int(word)
ValueError: invalid literal for int() with base 10: 'd'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers or 'quit' to quit: 83 81
Compute median / mode / mean: mean
The mean is 82.0
Enter a set of numbers or 'quit' to quit: 29 32
Compute median / mode / mean: k
Please enter a valid mode.
Compute median / mode / mean: k
Compute median / mode / mean: d
Please enter a valid mode.
Compute median / mode / mean: median
Compute median / mode / mean: median
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 79, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 61, in main
    print(median(sentence))
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 17, in median
    median = (list[num] + list[num + 1]) / 2
IndexError: list index out of range
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers or 'quit' to quit: 82 12
Compute median / mode / mean: j
Please enter a valid mode.
Compute median / mode / mean: d
Please enter a valid mode.
Compute median / mode / mean: median
The median is 47.0
Enter a set of numbers or 'quit' to quit: 21
Compute median / mode / mean: mode
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 78, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 64, in main
    print(mode(sentence))
TypeError: 'str' object is not callable
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter a set of numbers or 'quit' to quit: 12 12
Compute median / mode / mean: mean
The mean is 12.0
Enter a set of numbers or 'quit' to quit: 12 14
Compute median / mode / mean: median
The median is 13.0
Enter a set of numbers or 'quit' to quit: 12 14
Compute median / mode / mean: mode
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 75, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 61, in main
    print(mode(sentence))
TypeError: 'str' object is not callable
>>> dictionary = {}
>>> dictionary[1] = "hello"
>>> dictionary
{1: 'hello'}
>>> list
<class 'list'>
>>> list = "hello world"
>>> list.split()
['hello', 'world']
>>> dictionary[2] = list[2]
>>> dictionary
{1: 'hello', 2: 'l'}
>>> list
'hello world'
>>> list.split
<built-in method split of str object at 0x109b84630>
>>> list.split()
['hello', 'world']
>>> list
'hello world'
>>> list = list.split()
>>> dictionary[2] = list[2]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    dictionary[2] = list[2]
IndexError: list index out of range
>>> dictionary[2] = list[1]
>>> dictionary
{1: 'hello', 2: 'world'}
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name: test1.txt
The number of lines is 27
Enter a line number to print or 0 to quit: 1
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 94, in <module>
    print("The line is:", dictionary[num])
KeyError: '1'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name: test1.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 84, in <module>
    while line != "":
NameError: name 'line' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name: test1.txt
The number of lines is 5
Enter a line number to print or 0 to quit: 1
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 97, in <module>
    print("The line is:", dictionary[num])
KeyError: '1'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name: test1.txt
The number of lines is 5
Enter a line number to print or 0 to quit: 1
The line is: Bae, hello.
Enter a line number to print or 0 to quit: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name: test1.txt
The number of lines is 5
Enter a line number to print or 0 to quit: 3
The 3 line is: Hello world!
Enter a line number to print or 0 to quit: 2
The 2 line is: My name is hsiaoting.
Enter a line number to print or 0 to quit: 5
The 5 line is: Im fine!
Enter a line number to print or 0 to quit: 0
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 97, in <module>
    print("The", num, "line is:", dictionary[num])
KeyError: 0
>>> list
['Bae, hello.', 'My name is hsiaoting.', 'Hello world!', 'How are you?', 'Im fine!']
>>> tuple(list)
('Bae, hello.', 'My name is hsiaoting.', 'Hello world!', 'How are you?', 'Im fine!')
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 154, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 150, in main
    print(sentence())
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 136, in sentence
    return nounPhrase() + " " + verbPhrase()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 139, in nounPhrase
    return random.choice(articles) + " " + random.choice(nouns)
NameError: name 'articles' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: nouns.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 155, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 149, in main
    getWords()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 117, in getWords
    list.append(word)
AttributeError: 'str' object has no attribute 'append'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: nouns.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 155, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 151, in main
    print(sentence())
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 136, in sentence
    return nounPhrase() + " " + verbPhrase()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 139, in nounPhrase
    return random.choice(articles) + " " + random.choice(nouns)
NameError: name 'articles' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: nouns.txt
Enter the file to input: verbs.txt
Enter the file to input: articles.txt
Enter the file to input: prepositions.txt
Enter the file to input:  
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 155, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 149, in main
    getWords()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 112, in getWords
    f = open(fileName, "r")
FileNotFoundError: [Errno 2] No such file or directory: ' '
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: nouns.txt
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file to input: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: nouns.txt
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 154, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 148, in main
    getWords()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 121, in getWords
    print(nouns)
KeyboardInterrupt
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: nouns.txt
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file to input: verbs.txt
('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')
Enter the file to input: prepositions.txt
('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')
Enter the file to input: articles.txt
('A', 'AN', 'THE')
Enter the file to input:  
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 158, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 152, in main
    getWords()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 111, in getWords
    f = open(fileName, "r")
FileNotFoundError: [Errno 2] No such file or directory: ' '
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: verbs.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 158, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 151, in main
    number = int(input("Enter the number of sentences: "))
ValueError: invalid literal for int() with base 10: 'verbs.txt'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: verbs.txt
('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')
Enter the file to input: nouns.txt
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file to input: prepositions.txt
('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')
Enter the file to input: articles.txt
('A', 'AN', 'THE')
Enter the file to input: quit
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 158, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 154, in main
    print(sentence())
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 139, in sentence
    return nounPhrase() + " " + verbPhrase()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 142, in nounPhrase
    return random.choice(articles) + " " + random.choice(nouns)
NameError: name 'articles' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: verbs.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 157, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 153, in main
    print(sentence())
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 138, in sentence
    return nounPhrase() + " " + verbPhrase()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 141, in nounPhrase
    return random.choice(articles) + " " + random.choice(nouns)
NameError: name 'articles' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: verbs.txt
Enter the file to input: nouns.txt
Enter the file to input: articles.txt
Enter the file to input: prepositions.txt
Enter the file to input: quit
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 157, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 153, in main
    print(sentence())
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 138, in sentence
    return nounPhrase() + " " + verbPhrase()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 141, in nounPhrase
    return random.choice(articles) + " " + random.choice(nouns)
NameError: name 'articles' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: verbs.txt
('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')
Enter the file to input: articles.txt
('A', 'AN', 'THE')
Enter the file to input: prepositions.txt
('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')
Enter the file to input: nouns.txt
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file to input: quit
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 161, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 157, in main
    print(sentence())
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 142, in sentence
    return nounPhrase() + " " + verbPhrase()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 145, in nounPhrase
    return random.choice(articles) + " " + random.choice(nouns)
NameError: name 'articles' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: verbs.txt
('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')
Enter the file to input: nouns.txt
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file to input: prepositions.txt
('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')
Enter the file to input: articles.txt
('A', 'AN', 'THE')
Enter the file to input: quit
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 161, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 157, in main
    print(sentence())
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 142, in sentence
    return nounPhrase() + " " + verbPhrase()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 145, in nounPhrase
    return random.choice(verbs) + " " + random.choice(nouns)
NameError: name 'verbs' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: nouns.txt
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file to input: verbs.txt
('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file to input: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: verbs.txt
('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')
Enter the file to input: nouns.txt
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file to input: prepositions.txt
('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')
Enter the file to input: articles.txt
('A', 'AN', 'THE')
Enter the file to input: quit
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 162, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 158, in main
    print(sentence())
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 143, in sentence
    return nounPhrase() + " " + verbPhrase()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 146, in nounPhrase
    return random.choice(articles) + " " + random.choice(nouns)
NameError: name 'articles' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: verbs.txt
('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')
Enter the file to input: nouns.txt
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file to input: prepositions.txt
('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')
Enter the file to input: articles.txt
('A', 'AN', 'THE')
Enter the file to input: quit
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 162, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 158, in main
    print(sentence())
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 143, in sentence
    return nounPhrase() + " " + verbPhrase()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 146, in nounPhrase
    return random.choice(articles) + " " + random.choice(nouns)
NameError: name 'articles' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: nouns.txt
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file to input: verbs.txt
('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')
Enter the file to input: articles.txt
('A', 'AN', 'THE')
Enter the file to input: prepositions.txt
('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 156, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 152, in main
    print(sentence())
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 136, in sentence
    return nounPhrase() + " " + verbPhrase()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 139, in nounPhrase
    return random.choice(articles) + " " + random.choice(nouns)
NameError: name 'articles' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the number of sentences: 1
Enter the file to input: verbs.txt
('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')
Enter the file to input: nouns.txt
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file to input: prepositions.txt
('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')
Enter the file to input: articles.txt
('A', 'AN', 'THE')
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 158, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 149, in main
    print(nouns)
NameError: name 'nouns' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the noun file name: nouns.txt
Enter the verb file name: verbs.txt
Enter the preposition file name: prepositions.txt
Enter the article file name: articles.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 150, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 138, in main
    nouns = getWords(nouns)
TypeError: getWords() takes 0 positional arguments but 1 was given
>>> tuple = (1,2,3)
>>> tuple
(1, 2, 3)
>>> tuple = ()
>>> tuple
()
>>> fileName = "nouns.txt"
>>> fileName.strip(.txt)
SyntaxError: invalid syntax
>>> fileName.strip(".txt")
'nouns'
>>> fileName
'nouns.txt'
>>> list
<class 'list'>
>>> list = "hello my world"
>>> tuple(list)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    tuple(list)
TypeError: 'tuple' object is not callable
>>> list = ["hello", "world"]
>>> tuple(list)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    tuple(list)
TypeError: 'tuple' object is not callable
>>> tuple(list)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    tuple(list)
TypeError: 'tuple' object is not callable
>>> list = [hello, world]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    list = [hello, world]
NameError: name 'hello' is not defined
>>> list = ["hello", "world"]
>>> list
['hello', 'world']
>>> tuple.list()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    tuple.list()
AttributeError: 'tuple' object has no attribute 'list'
>>> tuple(list)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    tuple(list)
TypeError: 'tuple' object is not callable
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the nouns file name: nouns.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 169, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 154, in main
    getWords(fileName)
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 119, in getWords
    return fileName.strip(".txt")
AttributeError: 'tuple' object has no attribute 'strip'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
Enter the file name to import: verbs.txt
Enter the file name to import: prepositions.txt
Enter the file name to import: articles.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 169, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 158, in main
    print(nouns)
NameError: name 'nouns' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 169, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 156, in main
    getWords(fileName)
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 117, in getWords
    tuple = tuple(list)
TypeError: 'str' object is not callable
>>> tuple("list")
('l', 'i', 's', 't')
>>> list
<class 'list'>
>>> list = []
>>> list.append(hello)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    list.append(hello)
NameError: name 'hello' is not defined
>>> list.append("hello")
>>> list
['hello']
>>> list.append("world")
>>> list
['hello', 'world']
>>> tuple(list)
('hello', 'world')
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
Enter the file name to import: verbs.txt
Enter the file name to import: prepositions.txt
Enter the file name to import: articles.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 169, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 158, in main
    print(nouns)
NameError: name 'nouns' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 170, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 156, in main
    getWords()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 108, in getWords
    f = open(fileName, "r")
NameError: name 'fileName' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file name to import: verbs.txt
('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')
Enter the file name to import: articles.txt
('A', 'AN', 'THE')
Enter the file name to import: prepositions.txt
('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 170, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 159, in main
    print(nouns)
NameError: name 'nouns' is not defined
>>> list("string")
['s', 't', 'r', 'i', 'n', 'g']
>>> "string" = []
SyntaxError: cannot assign to literal
>>> list
<class 'list'>
>>> vars()['nouns']
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    vars()['nouns']
KeyError: 'nouns'
>>> vars(['nouns'])
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    vars(['nouns'])
TypeError: vars() argument must have __dict__ attribute
>>> dictionary = {"nouns.txt":nouns}
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    dictionary = {"nouns.txt":nouns}
NameError: name 'nouns' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file name to import: verbs.txt
('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')
Enter the file name to import: prepositions.txt
('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')
Enter the file name to import: articles.txt
('A', 'AN', 'THE')
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 165, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 154, in main
    print("nouns tuple:", nouns)
NameError: name 'nouns' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
['BOY']
['BOY', 'GIRL']
['BOY', 'GIRL', 'BAT']
['BOY', 'GIRL', 'BAT', 'BALL']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM']
['BOY']
['BOY', 'GIRL']
['BOY', 'GIRL', 'BAT']
['BOY', 'GIRL', 'BAT', 'BALL']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI']
['BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM']
('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')
Enter the file name to import: 
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 166, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 151, in main
    fileName = input("Enter the file name to import: ")
KeyboardInterrupt
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 145, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 128, in main
    x = getWords(fileName)
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 109, in getWords
    list = f.readlines().strip()
AttributeError: 'list' object has no attribute 'strip'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
{'nouns': ('BOY\n', 'GIRL\n', 'BAT\n', 'BALL\n', 'MOM\n', 'DAD\n', 'SISTER\n', 'BROTHER\n', 'FAN\n', 'CAT\n', 'DOG\n', 'HSIAOTING\n', 'ZHENGHONG\n', 'XINYI\n', 'SAM\n')}
Enter the file name to import: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 145, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 128, in main
    x = getWords(fileName)
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 109, in getWords
    list = f.readlines().rstrip()
AttributeError: 'list' object has no attribute 'rstrip'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')}
Enter the file name to import: verbs.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')}
Enter the file name to import: prepositions.txt
{'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')}
Enter the file name to import: articles.txt
{'articles': ('A', 'AN', 'THE')}
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 147, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 136, in main
    print("nouns tuple:", nouns)
NameError: name 'nouns' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')}
Enter the file name to import: verbs.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')}
Enter the file name to import: prepositions.txt
{'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')}
Enter the file name to import: articles.txt
{'articles': ('A', 'AN', 'THE')}
Enter the number of sentences: 1
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 142, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 138, in main
    print(sentence())
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 114, in sentence
    return nounPhrase() + " " + verbPhrase()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 117, in nounPhrase
    return random.choice(dictionary[articles]) + " " + \
NameError: name 'dictionary' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')}
Enter the file name to import: verbs.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')}
Enter the file name to import: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')}
Enter the file name to import: verbs.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')}
Enter the file name to import: prepositions.txt
{'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')}
Enter the file name to import: articles.txt
{'articles': ('A', 'AN', 'THE')}
{'articles': ('A', 'AN', 'THE')}
Enter the number of sentences: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py
Enter the file name to import: nouns.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')}
Enter the file name to import: verbs.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')}
Enter the file name to import: prepositions.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')}
Enter the file name to import: articles.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER'), 'articles': ('A', 'AN', 'THE')}
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER'), 'articles': ('A', 'AN', 'THE')}
Enter the number of sentences: 1
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 144, in <module>
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 140, in main
TypeError: sentence() missing 1 required positional argument: 'dictionary'
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py ===========
Enter the file name to import: nouns.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')}
Enter the file name to import: verbs.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')}
Enter the file name to import: prepositions.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')}
Enter the file name to import: articles.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER'), 'articles': ('A', 'AN', 'THE')}
Enter the number of sentences: 1
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 143, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 139, in main
    print(sentence())
TypeError: sentence() missing 1 required positional argument: 'dictionary'
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py ===========
Enter the file name to import: nouns.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')}
Enter the file name to import: prepositions.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')}
Enter the file name to import: articles.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER'), 'articles': ('A', 'AN', 'THE')}
Enter the file name to import: verbs.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER'), 'articles': ('A', 'AN', 'THE'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')}
Enter the number of sentences: 	1
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 143, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 139, in main
    print(sentence())
TypeError: sentence() missing 1 required positional argument: 'dictionary'
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py ===========
Enter the file name to import: nouns.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')}
Enter the file name to import: verbs.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')}
Enter the file name to import: prepositions.txt
{'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')}
Enter the file name to import: articles.tx
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 143, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 131, in main
    x = getWords(fileName)
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 108, in getWords
    f = open(fileName, "r")
FileNotFoundError: [Errno 2] No such file or directory: 'articles.tx'
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py ===========
Enter the file name to import: verbs.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')}
Enter the file name to import: nouns.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')}
Enter the file name to import: prepositions.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')}
Enter the file name to import: articles.
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 143, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 131, in main
    x = getWords(fileName)
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 108, in getWords
    f = open(fileName, "r")
FileNotFoundError: [Errno 2] No such file or directory: 'articles.'
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py ===========
Enter the file name to import: verbs.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')}
Enter the file name to import: nouns.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')}
Enter the file name to import: prepositions.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')}
Enter the file name to import: articles.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER'), 'articles': ('A', 'AN', 'THE')}
Enter the number of sentences: 1
AN BAT HIT A BOY UNDER AN DAD
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py ===========
>>> 
KeyboardInterrupt
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py ===========
Enter the file name to import: verbs.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED')}
Enter the file name to import: nouns.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM')}
Enter the file name to import: prepositions.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER')}
Enter the file name to import: articles.txt
{'verbs': ('HIT', 'SAW', 'LIKED', 'CLAPPED', 'SMELL', 'HEARD', 'RAN', 'WALKED', 'TALKED', 'STOOD', 'SANG', 'PLAYED'), 'nouns': ('BOY', 'GIRL', 'BAT', 'BALL', 'MOM', 'DAD', 'SISTER', 'BROTHER', 'FAN', 'CAT', 'DOG', 'HSIAOTING', 'ZHENGHONG', 'XINYI', 'SAM'), 'prepositions': ('WITH', 'BY', 'ABOUT', 'ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AROUND', 'BENEATH', 'BELOW', 'BESIDES', 'BETWEEN', 'BEYOND', 'FOR', 'IN', 'FROM', 'INTO', 'OF', 'ONTO', 'UNDER'), 'articles': ('A', 'AN', 'THE')}
Enter the number of sentences: 2
THE BROTHER SAW A GIRL WITH THE MOM
A BROTHER SMELL THE MOM OF THE SAM
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py ===========
Enter a set of numbers or 'quit' to quit: 12 13 42
Compute median / mode / mean: mode
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 73, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 62, in main
    print(mode(sentence))
TypeError: 'str' object is not callable
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py ===========
Enter a set of numbers or 'quit' to quit: 12 34 12
Compute median / mode / mean: mode
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 73, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 62, in main
    print(mode(sentence))
  File "/Users/hsiaotingluv/Desktop/python/20200502 (file).py", line 38, in mode
    return "The mode is " + key
TypeError: can only concatenate str (not "int") to str
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200502 (file).py ===========
Enter a set of numbers or 'quit' to quit: 12 34 12
Compute median / mode / mean: mode
The mode is 12
Enter a set of numbers or 'quit' to quit: 12 12 23
Compute median / mode / mean: mode
The mode is 12
Enter a set of numbers or 'quit' to quit: 19 19 22 22 22
Compute median / mode / mean: mode
The mode is 22
Enter a set of numbers or 'quit' to quit: quit
>>> 