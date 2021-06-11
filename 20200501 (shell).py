Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200501 (file).py ===========
Enter the number of sentences: 2
A BALL LIKED A GIRL WITH THE BOY
A BAT LIKED THE BAT BY THE GIRL
>>> info = {}
>>> info["name"] = "Sandy"
>>> info["occupation"] = "student"
>>> info
{'name': 'Sandy', 'occupation': 'student'}
>>> info["occupation"] = "programmer"
>>> info
{'name': 'Sandy', 'occupation': 'programmer'}
>>> info["name"]
'Sandy'
>>> info["Sandy"]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    info["Sandy"]
KeyError: 'Sandy'
>>> if "name" in info:
	print(info["name"])

	
Sandy
>>> info.["name"]
SyntaxError: invalid syntax
>>> info.get["name"]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    info.get["name"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> info.get["Sandy"]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    info.get["Sandy"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(info.get("job", None))
None
>>> print(info.get("name", None))
Sandy
>>> print(info.pop("job", None))
None
>>> print(info.pop("occupation", None))
programmer
>>> info
{'name': 'Sandy'}
>>> grades = {90:"A", 80:"B", 70:"C"}
>>> grades.items()
dict_items([(90, 'A'), (80, 'B'), (70, 'C')])
>>> list(grades.items())
[(90, 'A'), (80, 'B'), (70, 'C')]
>>> for (key, value) in grades.items():
	print(key, value)

	
90 A
80 B
70 C
>>> info
{'name': 'Sandy'}
>>> info.keys)_
SyntaxError: unmatched ')'
>>> info.keys()
dict_keys(['name'])
>>> info["occupation"] = "student"
>>> info
{'name': 'Sandy', 'occupation': 'student'}
>>> theKeys = list(info.keys())
>>> theKeys.sort()
>>> for key in theKeys:
	print(key, info[key])

	
name Sandy
occupation student
>>> info[occupation]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    info[occupation]
NameError: name 'occupation' is not defined
>>> info["occupation"]
'student'
>>> len(info)
2
>>> info[key]
'student'
>>> info
{'name': 'Sandy', 'occupation': 'student'}
>>> info.get("occupation", default)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    info.get("occupation", default)
NameError: name 'default' is not defined
>>> info.get("occupation"[, default])
SyntaxError: invalid syntax
>>> info.get("occupation", [default])
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    info.get("occupation", [default])
NameError: name 'default' is not defined
>>> info.get("occupation", None)
'student'
>>> list(info.items())
[('name', 'Sandy'), ('occupation', 'student')]
>>> list(info.values())
['Sandy', 'student']
>>> hexToBinaryTable = {'0':'0000', '1':'0001', '2':'0010', \
		    '3':'0011', '4':'0100', '5':'0101', \
		    '6':'0110', '7':'0111', '8':'1000', \
		    '9':'1001', 'A':'1010', 'B':'1011', \
		    'C':'1100', 'D':'1101', 'E':'1110', \'F':'1111'}
		    
SyntaxError: unexpected character after line continuation character
>>> hexToBinaryTable = {'0':'0000', '1':'0001', '2':'0010', \
		    '3':'0011', '4':'0100', '5':'0101', \
		    '6':'0110', '7':'0111', '8':'1000', \
		    '9':'1001', 'A':'1010', 'B':'1011', \
		    'C':'1100', 'D':'1101', 'E':'1110', \'F':'1111'}
		    
SyntaxError: unexpected character after line continuation character
>>> hexToBinaryTable = {'0':'0000', '1':'0001', '2':'0010', \
		    '3':'0011', '4':'0100', '5':'0101', \
		    '6':'0110', '7':'0111', '8':'1000', \
		    '9':'1001', 'A':'1010', 'B':'1011', \
		    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
>>> def convert(number, table):
	binary = ""
	for digit in number"
	
SyntaxError: EOL while scanning string literal
>>> def convert(number, table):
	binary = ""
	for digit in number:
		binary += table[digit]
	return binary

>>> convert("35A", hexToBinaryTable)
'001101011010'
>>> info
{'name': 'Sandy', 'occupation': 'student'}
>>> info.values()
dict_values(['Sandy', 'student'])
>>> max(info.values())
'student'
>>> data["me"] = 2
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    data["me"] = 2
NameError: name 'data' is not defined
>>> data["me"] = "2"
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    data["me"] = "2"
NameError: name 'data' is not defined
>>> data = {}
>>> data["me"] = 2
>>> data
{'me': 2}
>>> data["you"] = 3
>>> data.value()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    data.value()
AttributeError: 'dict' object has no attribute 'value'
>>> data.values()
dict_values([2, 3])
>>> max(data.values())
3
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200501 (file).py ===========
Enter the filename: test1.txt
The mode is BAE,
>>> len(info)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    len(info)
NameError: name 'info' is not defined
>>> info
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    info
NameError: name 'info' is not defined
>>> dara
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    dara
NameError: name 'dara' is not defined
>>> data
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    data
NameError: name 'data' is not defined
>>> data = {}
>>> data["me"] = 2
>>> data["you"] = 3
>>> len(data)
2
>>> data.pop("you")
3
>>> data
{'me': 2}
>>> data.sort
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    data.sort
AttributeError: 'dict' object has no attribute 'sort'
>>> data
{'me': 2}
>>> data = {"b": -20, "a": 35, "c":40}
>>> data
{'b': -20, 'a': 35, 'c': 40}
>>> keys = list(data.keys())
>>> keys
['b', 'a', 'c']
>>> keys.sort()
>>> keys
['a', 'b', 'c']
>>> for key in keys:
	print(key, data[key])

	
a 35
b -20
c 40
>>> answer = "Hello my name is hsiaoting"
>>> for word in answer:
	print(word)

	
H
e
l
l
o
 
m
y
 
n
a
m
e
 
i
s
 
h
s
i
a
o
t
i
n
g
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200501 (file).py ===========
>>> 
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200501 (file).py ===========
Good morning, I hope you are well today. 
 What can I do for you? 
 My mother and I don't get along
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200501 (file).py", line 84, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200501 (file).py", line 81, in main
    print(reply())
  File "/Users/hsiaotingluv/Desktop/python/20200501 (file).py", line 70, in reply
    words = list(answer.split())
NameError: name 'answer' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200501 (file).py ===========
Good morning, I hope you are well today. 
 What can I do for you? 
My mother and I don't get along
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200501 (file).py", line 84, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200501 (file).py", line 81, in main
    print(reply())
  File "/Users/hsiaotingluv/Desktop/python/20200501 (file).py", line 70, in reply
    words = list(answer.split())
NameError: name 'answer' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200501 (file).py ===========
Good morning, I hope you are well today. 
What can I do for you? 
My mother and I don't get along
Can you explain why
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200501 (file).py ===========
Good morning, I hope you are well today. 
What can I do for you? 
My mother and I don't get along
[]
Can you explain why
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200501 (file).py ===========
Good morning, I hope you are well today. 
What can I do for you? 
My mother and I don't get along
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200501 (file).py", line 86, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200501 (file).py", line 83, in main
    print(reply())
  File "/Users/hsiaotingluv/Desktop/python/20200501 (file).py", line 72, in reply
    for word in words:
NameError: name 'words' is not defined
>>> replacements = {"I":"you", "me":"you", "my":"your","we":"you", "us":"you", "mine":"yours"}
>>> replyWords = []
>>> sentence = "hello my name is hsiao ting"
>>> words = sentence.split()
>>> words
['hello', 'my', 'name', 'is', 'hsiao', 'ting']
>>> for word in words:
	replyWords.append(replacements.get(word, word))

	
>>> print replyWords
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(replyWords)?
>>> print(replyWords)
['hello', 'your', 'name', 'is', 'hsiao', 'ting']
>>> for word in words:
	replyWords.append(replacements.get(word, word))
	print(replyWords)

	
['hello', 'your', 'name', 'is', 'hsiao', 'ting', 'hello']
['hello', 'your', 'name', 'is', 'hsiao', 'ting', 'hello', 'your']
['hello', 'your', 'name', 'is', 'hsiao', 'ting', 'hello', 'your', 'name']
['hello', 'your', 'name', 'is', 'hsiao', 'ting', 'hello', 'your', 'name', 'is']
['hello', 'your', 'name', 'is', 'hsiao', 'ting', 'hello', 'your', 'name', 'is', 'hsiao']
['hello', 'your', 'name', 'is', 'hsiao', 'ting', 'hello', 'your', 'name', 'is', 'hsiao', 'ting']
>>> replacements.get(word)
>>> replacements.get(word,word)
'ting'
>>> " ".join(replyWords)
'hello your name is hsiao ting hello your name is hsiao ting'
>>> replyWords
['hello', 'your', 'name', 'is', 'hsiao', 'ting', 'hello', 'your', 'name', 'is', 'hsiao', 'ting']
>>> print(replyWords)
['hello', 'your', 'name', 'is', 'hsiao', 'ting', 'hello', 'your', 'name', 'is', 'hsiao', 'ting']
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200501 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>>  My mother and I don't get along
Can you explain whyMy mother and you don't get along

>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200501 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> My mother and I don't get along
Can you explain why your mother and i don't get along

>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200501 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> My mother and I don't get along
Can you explain why your mother and you don't get along

>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200501 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> My mother and I don't get along
You seem to think that your mother and you don't get along?

>> she always favors my sister
Please tell me more.

>>  my dad and I get along fine
You seem to think that your dad and you get along fine?

>>  he helps me with my homework
You seem to think that he helps you with your homework?

>>  he helps me with my homework
Why do you say that he helps you with your homework?

>> she always favors my sister
You seem to think that she always favors your sister?

>> she always favors my sister
Can you explain why she always favors your sister?

>> she always favors my sister
You seem to think that she always favors your sister?

>> she always favors my sister
Why do you say that she always favors your sister?

>> quit
Have a nice day!
>>> 