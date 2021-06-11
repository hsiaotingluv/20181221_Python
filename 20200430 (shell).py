Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = list(range(1,5))
>>> a
[1, 2, 3, 4]
>>> a[1]
2
>>> b = list(range(5,9))
>>> a + b
[1, 2, 3, 4, 5, 6, 7, 8]
>>> len(a)
4
>>> a[2] = 0
>>> a
[1, 2, 0, 4]
>>> numbers = [2, 3, 4, 5]
>>> numbers
[2, 3, 4, 5]
>>> for index in range(len(numbers)):
	numbers[index] = numbers[index] ** 2

	
>>> numbers
[4, 9, 16, 25]
>>> sentence = "This example has five words."
>>> words = sentence.split()
>>> words
['This', 'example', 'has', 'five', 'words.']
>>> for index in range(len(words)):
	words[index] = words[index].upper()

	
>>> words
['THIS', 'EXAMPLE', 'HAS', 'FIVE', 'WORDS.']
>>> words.insert(1, 10)
>>> words
['THIS', 10, 'EXAMPLE', 'HAS', 'FIVE', 'WORDS.']
>>> words.append(3)
>>> words
['THIS', 10, 'EXAMPLE', 'HAS', 'FIVE', 'WORDS.', 3]
>>> words.extend([2, 3, 12])
>>> words
['THIS', 10, 'EXAMPLE', 'HAS', 'FIVE', 'WORDS.', 3, 2, 3, 12]
>>> words + [12, 13]
['THIS', 10, 'EXAMPLE', 'HAS', 'FIVE', 'WORDS.', 3, 2, 3, 12, 12, 13]
>>> words
['THIS', 10, 'EXAMPLE', 'HAS', 'FIVE', 'WORDS.', 3, 2, 3, 12]
>>> words.pop
<built-in method pop of list object at 0x1089ea7c0>
>>> words
['THIS', 10, 'EXAMPLE', 'HAS', 'FIVE', 'WORDS.', 3, 2, 3, 12]
>>> words.pop()
12
>>> words.pop(2)
'EXAMPLE'
>>> words
['THIS', 10, 'HAS', 'FIVE', 'WORDS.', 3, 2, 3]
>>> list = [34, 45, 67]
>>> target = 45
>>> if target in list:
	print(list.index(target))
else:
	print(-1)

	
1
>>> list.index(0)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    list.index(0)
ValueError: 0 is not in list
>>> list.index(67)
2
>>> words.sort()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    words.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> words
['THIS', 10, 'HAS', 'FIVE', 'WORDS.', 3, 2, 3]
>>> words.pop(1)
10
>>> numbers = [1, 5, 2, 7, 4]
>>> numbers.sort()
>>> numbers
[1, 2, 4, 5, 7]
>>> first = [10, 20, 30]
>>> second = first
>>> first
[10, 20, 30]
>>> second
[10, 20, 30]
>>> first[1] = 99
>>> first
[10, 99, 30]
>>> second
[10, 99, 30]
>>> third = []
>>> for element in first:
	third.append(element)

	
>>> first
[10, 99, 30]
>>> third
[10, 99, 30]
>>> first[1] = 2
>>> first
[10, 2, 30]
>>> third
[10, 99, 30]
>>> third = list(first)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    third = list(first)
TypeError: 'list' object is not callable
>>> 6 // 2
3
>>> 6 / 2
3.0
>>> 5 // 2
2
>>> 5 % 2
1
>>> numbers
[1, 2, 4, 5, 7]
>>> numbers.insert(9)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    numbers.insert(9)
TypeError: insert expected 2 arguments, got 1
>>> numbers.append(9)
>>> numbers
[1, 2, 4, 5, 7, 9]
>>> data = [5, 3, 7]
>>> data
[5, 3, 7]
>>> data[2]
7
>>> data[-1]
7
>>> tuple(data)
(5, 3, 7)
>>> data
[5, 3, 7]
>>> data[0] = -5
>>> data
[-5, 3, 7]
>>> data.append(10)
>>> data
[-5, 3, 7, 10]
>>> data.insert(2, 22)
>>> data
[-5, 3, 22, 7, 10]
>>> data.pop(1)
3
>>> newData = [1, 2, 3]
>>> data = data + newData
>>> data
[-5, 22, 7, 10, 1, 2, 3]
>>> data.index(7)
2
>>> data.sort()
>>> data
[-5, 1, 2, 3, 7, 10, 22]
>>> 