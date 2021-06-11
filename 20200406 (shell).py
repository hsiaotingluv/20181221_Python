Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> str = 'i love zheng hong'
>>> str = str[:6] + ' tong' + str[6:]
>>> str
'i love tong zheng hong'
>>> str.center(40)
'         i love tong zheng hong         '
>>> str.center(10)
'i love tong zheng hong'
>>> str.count('ng')
3
>>> "{0} love {1} {2}".format("I", "zheng", "hong")
'I love zheng hong'
>>> "{a} love {b} {c}".format(a = "I", b = "zheng", c = "hong")
'I love zheng hong'
>>> "{0} love {b} {c}".format("I", b = "zheng", c = "hong")
'I love zheng hong'
>>> "{a} love {0} {c}".format(a = "I", "zheng", c = "hong")
SyntaxError: positional argument follows keyword argument
>>> print("\\ta")
\ta
>>> print("{{0}}".format("不打印"))
{0}
>>> print("//")
//
>>> print("\\")
\
>>> print("\t \\a")
	 \a
>>> print("{}")
{}
>>> print("{0}")
{0}
>>> "{0:1f}{1}".format(27.658, "GB")
'27.658000GB'
>>> "{0:.1f}{1}".format(27.658, "GB")
'27.7GB'
>>> "%c" % 97
'a'
>>> '%c' % 109
'm'
>>> '%c %c %c' % (97, 98, 99)
'a b c'
>>> '%s' % 'I love you'
'I love you'
>>> '%4c %4c %4c' % (97, 98, 99)
'   a    b    c'
>>> '%5.1f' % 27.658
' 27.7'
>>> '%e.2f' % 27.658
'2.765800e+01.2f'
>>> '%.2e' % 27.658
'2.77e+01'
>>> '%-10d' % 5
'5         '
>>> '%+d' % 5
'+5'
>>> '%#o' % 10
'0o12'
>>> '%#X' % 10
'0XA'
>>> '%#X' % 108
'0X6C'
>>> '%010d' % 5
'0000000005'
>>> '%-010d' % 5
'5         '
>>> a = 'i love zheng hong'
>>> a = list(a)
>>> a
['i', ' ', 'l', 'o', 'v', 'e', ' ', 'z', 'h', 'e', 'n', 'g', ' ', 'h', 'o', 'n', 'g']
>>> b = (1, 1, 2, 3, 5, 8, 13, 21, 34)
>>> b = list(c)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    b = list(c)
NameError: name 'c' is not defined
>>> b = list(b)
>>> b
[1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> tuple(b)
(1, 1, 2, 3, 5, 8, 13, 21, 34)
>>> b
[1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> a
['i', ' ', 'l', 'o', 'v', 'e', ' ', 'z', 'h', 'e', 'n', 'g', ' ', 'h', 'o', 'n', 'g']
>>> len(a)
17
>>> max(1,2,3,4,5)
5
>>> max(B)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    max(B)
NameError: name 'B' is not defined
>>> max(b)
34
>>> max(a)
'z'
>>> numbers = [1, 18, 13, 9, -98, 34, 54,76, 32]
>>> max(numbers)
76
>>> min(76)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    min(76)
TypeError: 'int' object is not iterable
>>> min(numbers)
-98
>>> chars = '1234567890'
>>> min(chars)
'0'
>>> chars = 'abcdefj'
>>> max(chars)
'j'
>>> tuple = (1,2,3,4,5,6,7,8,9,0)
>>> max(tuple)
9
>>> numbers
[1, 18, 13, 9, -98, 34, 54, 76, 32]
>>> numbers.append('a')
>>> numbers
[1, 18, 13, 9, -98, 34, 54, 76, 32, 'a']
>>> tuple
(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
>>> tuple.append('a)
	     
SyntaxError: EOL while scanning string literal
>>> tuple.append('a')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    tuple.append('a')
AttributeError: 'tuple' object has no attribute 'append'
>>> tuple1 = (3.2, 2.4, 5.3)
>>> sum(tuple1)
10.899999999999999
>>> 
>>> numbers
[1, 18, 13, 9, -98, 34, 54, 76, 32, 'a']
>>> numbers.pop()
'a'
>>> numbers
[1, 18, 13, 9, -98, 34, 54, 76, 32]
>>> sum(numbers)
139
>>> help.list
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    help.list
AttributeError: '_Helper' object has no attribute 'list'
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> list.sorted()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    list.sorted()
AttributeError: type object 'list' has no attribute 'sorted'
>>> sorted(numbers)
[-98, 1, 9, 13, 18, 32, 34, 54, 76]
>>> reversed(numbers)
<list_reverseiterator object at 0x10f0580a0>
>>> list(reversed(numbers))
[32, 76, 54, 34, -98, 9, 13, 18, 1]
>>> enumerate(numbers)
<enumerate object at 0x10bdb74c0>
>>> list(enumerate(numbers))
[(0, 1), (1, 18), (2, 13), (3, 9), (4, -98), (5, 34), (6, 54), (7, 76), (8, 32)]
>>> numbers[5]
34
>>> a = [1, 2, 3, 4, 5, 6, 7, 8]
>>> b = [4, 5, 6, 7, 8]
>>> zip(a,b)
<zip object at 0x10bd88640>
>>> zip(a, b)
<zip object at 0x10bdb9f40>
>>> list(zip(a, b))
[(1, 4), (2, 5), (3, 6), (4, 7), (5, 8)]
>>> def myFirstFunction():
	print("hello world")
	print("my name is hsiaoting")
	print("nice to meet you")

	
>>> myFirstFunction
<function myFirstFunction at 0x10f0570d0>
>>> myFirstFunction()
hello world
my name is hsiaoting
nice to meet you
>>> mySecondFunction()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    mySecondFunction()
NameError: name 'mySecondFunction' is not defined
>>> myFirstFunction()
hello world
my name is hsiaoting
nice to meet you
>>> myFirstFunction(2)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    myFirstFunction(2)
TypeError: myFirstFunction() takes 0 positional arguments but 1 was given
>>> myFirstFunction()
hello world
my name is hsiaoting
nice to meet you



>>> myFirstFunction()
hello world
my name is hsiaoting
nice to meet you
>>> def mySecondFunction(name):
	print("hello world")
	print("my name is" + name)
	print("nice to meet you")

	
>>> mySecondFunction('hsiaoting')
hello world
my name ishsiaoting
nice to meet you
>>> def add(num1, num2):
	sum = num1 + num2
	print(sum)

	
>>> add(1, 4)
5
>>> def add(num1, num2, num3, num4, num5):
	sum = num1 + num2 + num3 + num4 + num5
	print(sum)

	
>>> add(1, 3)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    add(1, 3)
TypeError: add() missing 3 required positional arguments: 'num3', 'num4', and 'num5'
>>> add(1, 3, 2, 4, 1)
11
>>> def add(num1, num2):
	return(num1 + num2)

>>> print(add(5, 6))
11
>>> 
>>> member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
>>> member.insert(1, "88", 3, "90")
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    member.insert(1, "88", 3, "90")
TypeError: insert expected 2 arguments, got 4
>>> member.insert(1, "88")
>>> member.append("90", 3)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    member.append("90", 3)
TypeError: append() takes exactly one argument (2 given)
>>> member.append("90")
>>> member
['小甲鱼', '88', '黑夜', '迷途', '怡静', '秋舞斜阳', '90']
>>> member.pop()
'90'
>>> member
['小甲鱼', '88', '黑夜', '迷途', '怡静', '秋舞斜阳']
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200406 (file).py ===========
['小甲鱼', '88', '黑夜', '90', '迷途', '85', '怡静', '90', '秋舞斜阳', '88']
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200406 (file).py ===========
['小甲鱼', '88', '黑夜', '90', '迷途', '85', '怡静', '90', '秋舞斜阳', '88']
小甲鱼
88
黑夜
90
迷途
85
怡静
90
秋舞斜阳
88
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200406 (file).py ===========
['小甲鱼', '88', '黑夜', '90', '迷途', '85', '怡静', '90', '秋舞斜阳', '88']
小甲鱼
88
黑夜
90
迷途
85
怡静
90
秋舞斜阳
88
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200406 (file).py", line 15, in <module>
    print(names, end = names(names + 1))
TypeError: can only concatenate str (not "int") to str
>>> names
'小甲鱼'
>>> names.append(88)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    names.append(88)
AttributeError: 'str' object has no attribute 'append'
>>> member
['小甲鱼', '88', '黑夜', '90', '迷途', '85', '怡静', '90', '秋舞斜阳', '88']
>>> member.append(88)
>>> member
['小甲鱼', '88', '黑夜', '90', '迷途', '85', '怡静', '90', '秋舞斜阳', '88', 88]
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200406 (file).py ===========
['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
小甲鱼
88
黑夜
90
迷途
85
怡静
90
秋舞斜阳
88
>>> member
['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200406 (file).py ===========
['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
小甲鱼
88
黑夜
90
迷途
85
怡静
90
秋舞斜阳
88
小甲鱼 88
黑夜 90
迷途 85
怡静 90
秋舞斜阳 88
小甲鱼 88
黑夜 90
迷途 85
怡静 90
秋舞斜阳 88
>>> list = [1, 2, 3, 4, 5]
>>> list
[1, 2, 3, 4, 5]
>>> list[0] == list [0;1]
SyntaxError: invalid syntax
>>> list[0] == list [0:1]
False
>>> list[0]
1
>>> list [0:1]
[1]
>>> list
[1, 2, 3, 4, 5]
>>> list.pop()
5
>>> list.insert(0, 5)
>>> list
[5, 1, 2, 3, 4]
>>> list[-1]
4
>>> list = list1
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    list = list1
NameError: name 'list1' is not defined
>>> list1 = list
>>> list1
[5, 1, 2, 3, 4]
>>> list
[5, 1, 2, 3, 4]
>>> list1
[5, 1, 2, 3, 4]
>>> list3 = list[:]
>>> list3
[5, 1, 2, 3, 4]
>>> list1
[5, 1, 2, 3, 4]
>>> list
[5, 1, 2, 3, 4]
>>> >>> old = [1, 2, 3, 4, 5]
>>> new = old
>>> old = [6]
>>> print(new)
SyntaxError: invalid syntax
>>> old = [1, 2, 3, 4, 5]
>>> new = old
>>> old = [6]
>>> print(new)
SyntaxError: multiple statements found while compiling a single statement
>>> old = [1,2,3,4,5]
>>> new = old
>>> old = [6]
>>> print(new)
[1, 2, 3, 4, 5]
>>> list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
>>> list1
[1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
>>> list1.replace('小甲鱼', '小鱿鱼')
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    list1.replace('小甲鱼', '小鱿鱼')
AttributeError: 'list' object has no attribute 'replace'
>>> help(list)
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 