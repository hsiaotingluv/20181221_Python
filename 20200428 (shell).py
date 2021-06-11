Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200404(file).py ===========
bae, 1
hello
bae, 2
hello. 1
hello. 4
name 1
name 3
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200404(file).py", line 23, in <module>
    if (word[position] in vowels) and (word[position + 1] in vowels):
IndexError: string index out of range
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200404(file).py ===========
bae, 1
hello
bae, 2
hello. 1
hello. 4
name 1
name 3
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200404(file).py", line 23, in <module>
    if (word[position + 1] in vowels):
IndexError: string index out of range
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200404(file).py ===========
bae, 1
hello
bae, 2
hello
hello. 1
hello
hello. 4
hello
name 1
hello
name 3
hello
is 0
hello
bae. 1
hello
bae. 2
hello
There are 2 sentences
There are 6 words
There are -1 syllables
The Flesch index is 218
The grade-level equivalent is -16
>>> 
============ RESTART: /Users/hsiaotingluv/Desktop/python/20200404(file).py ===========
bae, 1
a e
double
bae, 2
e ,
hello. 1
e l
hello. 4
o .
name 1
a m
name 3
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200404(file).py", line 22, in <module>
    print(word[position], word[position + 1])
IndexError: string index out of range
>>> names = "hsiaoting, zhenghong, xinyi, sam"
>>> names.append()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    names.append()
AttributeError: 'str' object has no attribute 'append'
>>> names.extend()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    names.extend()
AttributeError: 'str' object has no attribute 'extend'
>>> names.reverse()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    names.reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> list = names.split()
>>> list
['hsiaoting,', 'zhenghong,', 'xinyi,', 'sam']
>>> list.reverse()
>>> print(list.reverse())
None
>>> print(list.append())
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(list.append())
TypeError: append() takes exactly one argument (0 given)
>>> list.append("hello")
>>> list
['hsiaoting,', 'zhenghong,', 'xinyi,', 'sam', 'hello']
>>> list1 = "hi", "my", "name"
>>> list1
('hi', 'my', 'name')
>>> list1 = ["hi", "my", "name"]
>>> list1
['hi', 'my', 'name']
>>> list.extend()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list.extend()
TypeError: extend() takes exactly one argument (0 given)
>>> list.extend(list1)
>>> list
['hsiaoting,', 'zhenghong,', 'xinyi,', 'sam', 'hello', 'hi', 'my', 'name']
>>> list.count("s")
0
>>> list.count("hsiaoting")
0
>>> list.count("name")
1
>>> list.remove()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> list.remove(3)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list.remove(3)
ValueError: list.remove(x): x not in list
>>> list.remove(",")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list.remove(",")
ValueError: list.remove(x): x not in list
>>> list.remove(", ")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list.remove(", ")
ValueError: list.remove(x): x not in list
>>> list.remove("hi")
>>> list
['hsiaoting,', 'zhenghong,', 'xinyi,', 'sam', 'hello', 'my', 'name']
>>> list.pop()
'name'
>>> list
['hsiaoting,', 'zhenghong,', 'xinyi,', 'sam', 'hello', 'my']
>>> list.sort()
>>> list
['hello', 'hsiaoting,', 'my', 'sam', 'xinyi,', 'zhenghong,']
>>> list.insert("hi", 3)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list.insert("hi", 3)
TypeError: 'str' object cannot be interpreted as an integer
>>> list.insert("hi")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    list.insert("hi")
TypeError: insert expected 2 arguments, got 1
>>> list.insert(2, "hi")
>>> list
['hello', 'hsiaoting,', 'hi', 'my', 'sam', 'xinyi,', 'zhenghong,']
>>> list.reverse()
>>> list
['zhenghong,', 'xinyi,', 'sam', 'my', 'hi', 'hsiaoting,', 'hello']
>>> list.index(1)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    list.index(1)
ValueError: 1 is not in list
>>> list.index()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    list.index()
TypeError: index expected at least 1 argument, got 0
>>> list.index("sam")
2
>>> list.find("sam")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list.find("sam")
AttributeError: 'list' object has no attribute 'find'
>>> "%c" % 97
'a'
>>> "%c %c %c" % (97, 98, 99)
'a b c'
>>> "%s" % "I love you"
'I love you'
>>> "%d + %d = %d" % (4, 5, 4 + 5)
'4 + 5 = 9'
>>> "%o" % 10
'12'
>>> "%x" % 10
'a'
>>> "%X" % 10
'A'
>>> "%X" % 160
'A0'
>>>  "%+d" % 5
 
SyntaxError: unexpected indent
>>> "%+d" % 5
'+5'
>>> "%#o" % 10
'0o12'
>>> "%#X" % 10
'0XA'
>>> "%#X" % 103
'0X67'
>>> "%#d" % 103
'103'
>>> "%010d" % 5
'0000000005'
>>> "%-010d" % 5
'5         '
>>> a = "I love hsiaoting"
>>> a = list(a)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a = list(a)
TypeError: 'list' object is not callable
>>> b = (1, 1, 2, 3, 5, 8, 13, 21, 34)
>>> b = list(b)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    b = list(b)
TypeError: 'list' object is not callable
>>> numbers = [32, 44, 92, 44, -12, 24, 109, 0]
>>> sorted(numbers)
[-12, 0, 24, 32, 44, 44, 92, 109]
>>> reversed(numbers)
<list_reverseiterator object at 0x10ff0ba90>
>>> list(reversed(numbers))
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    list(reversed(numbers))
TypeError: 'list' object is not callable
>>> sum(numbers)
333
>>> enumerate(numbers)
<enumerate object at 0x10fe08ac0>
>>> list(enumerate(numbers))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    list(enumerate(numbers))
TypeError: 'list' object is not callable
>>> a = [1, 2, 3, 4, 5, 6, 7, 8]
>>> b = [4, 5, 6, 7, 8]
>>> zip(a, b)
<zip object at 0x10e566200>
>>> list(zip(a, b))
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    list(zip(a, b))
TypeError: 'list' object is not callable
>>> 