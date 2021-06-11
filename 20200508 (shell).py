Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py ========
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory

/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory

/Users/hsiaotingluv
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 5
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 120, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 62, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 62, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 51, in runCommand
    sizeCWD(os.getcwd()))
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 103, in sizeCWD
    size += sizeCWD(os.getcwd())
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 103, in sizeCWD
    size += sizeCWD(os.getcwd())
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 103, in sizeCWD
    size += sizeCWD(os.getcwd())
  [Previous line repeated 1014 more times]
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 99, in sizeCWD
    if os.path.isfile(element):
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/genericpath.py", line 30, in isfile
    st = os.stat(path)
RecursionError: maximum recursion depth exceeded while calling a Python object
>>> 
======== RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py ========
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory

/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 
2
Enter a number: 

/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory

/Users/hsiaotingluv
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 5

================================ RESTART: Shell ================================
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py ===========
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory

/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 5
The total number of bytes is 23555370658

/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 7

/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py ===========
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 7

Have a nice day!
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py ===========
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory

/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 3
Enter the name of directory: Desktop
ERROR: The directory does not exist

/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 3
Enter the name of directory: none
ERROR: The directory does not exist

/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory

/Users/hsiaotingluv
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 3
Enter the name of directory: Desktop
You have moved to the next directory

/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 7

Have a nice day!
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py ===========
>>> 
KeyboardInterrupt
>>> x = 5
>>> def f():
	x = 10

>>> f()
>>> print(x)
5
>>> def f():
	x = 10
	return x

>>> f()
10
>>> print(x)
5
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 13, in <module>
    print("The absolute values are: ", " ".join(absValues))
TypeError: sequence item 0: expected str instance, int found
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: 
-1,0,9,-9,-3,3
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 9, in <module>
    num = int(num)
ValueError: invalid literal for int() with base 10: ''
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
The absolute values are:  [ 0 ,   9 ,   3 ]
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
The absolute values are:  [0, 9, 3]
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 26, in <module>
    "".join(map(absValues, numbers.split(",")))
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 23, in absValues
    if num >= 0:
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 24, in <module>
    "".join(map(absValues, numbers.split(",")))
TypeError: sequence item 0: expected str instance, NoneType found
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
<map object at 0x1087bdd60>
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 18, in <module>
    print(map(abs, numList))
NameError: name 'numList' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
<map object at 0x10ce82d60>
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
Absolute values are:<map object at 0x10e8c2d60>
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 17, in <module>
    absValues = list(map(abs, numbers))
TypeError: bad operand type for abs(): 'str'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: numList = numbers.split(",")
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 19, in <module>
    absValues = list(map(abs, int(numList)))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 9, in <module>
    absValues.append(abs(num))
TypeError: bad operand type for abs(): 'str'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
The absolute values are:  [1, 0, 9, 9, 3, 3]
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
[1]
[1, 0]
[1, 0, 9]
[1, 0, 9, 9]
[1, 0, 9, 9, 3]
[1, 0, 9, 9, 3, 3]
The absolute values are:  [1, 0, 9, 9, 3, 3]
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 11, in <module>
    print("The absolute values are: ", "".join(absValues))
TypeError: sequence item 0: expected str instance, int found
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
The absolute values are:  [1, 0, 9, 9, 3, 3]
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
The absolute values are:  [ 1 ,   0 ,   9 ,   9 ,   3 ,   3 ]
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
The absolute values are:  109933
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
The absolute values are:  1,0,9,9,3,3
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
['-1', '0', '9', '-9', '-3', '3']
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 25, in <module>
    print("Absolute values are:" + list(absValues))
TypeError: bad operand type for abs(): 'str'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 16, in <module>
    numbers = int(input("Enter a list of numbers: "))
ValueError: invalid literal for int() with base 10: '-1,0,9,-9,-3,3'
>>> -1 0
SyntaxError: invalid syntax
>>> 
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 18, in <module>
    print("Absolute values are:" + list(map(abs, inputList)))
TypeError: can only concatenate str (not "list") to str
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 19, in <module>
    print("Absolute values are:" + list(absValues))
TypeError: can only concatenate str (not "list") to str
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 18, in <module>
    print("Absolute values are:" + map(abs, inputList))
TypeError: can only concatenate str (not "map") to str
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Absolute values are: <map object at 0x107042130>
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Absolute values are: [1, 7, 9, 3]
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 24, in <module>
    list(filter(positive, range(inputList)))
NameError: name 'positive' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
[1, 7, 3]
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
helloworldmy nameishsiaoting
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
hello world my name is hsiaoting
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 30, in <module>
    s
NameError: name 's' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
hello world my name is hsiaoting
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
Absolute values are: [1.0, 0.0, 9.0, 9.0, 3.0, 3.0]
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter a list of numbers: -1,0,9,-9,-3,3
Absolute values are: [1, 0, 9, 9, 3, 3]
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter the lower bound, upper bound and step value: 1,10
Enter the function: 
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 42, in <module>
    lower, upper, step = num.split(",")
ValueError: not enough values to unpack (expected 3, got 2)
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter the lower bound: 1
Enter the upper bound: 100
Enter the step value: 
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 42, in <module>
    step = int(input("Enter the step value: "))
ValueError: invalid literal for int() with base 10: ''
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter the lower bound: 1
Enter the upper bound: 100
Enter the step value: 1
Enter the function: 
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter the lower bound: 1
Enter the upper bound: 100
Enter the step value: 1
Enter the function: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter the lower bound: 1
Enter the upper bound: 10
Enter the step value: 1
Enter the function: math.sqrt
>>> 
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter the lower bound: 1
Enter the upper bound: 10
Enter the step value: 1
Enter the function: math.sqrt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 48, in <module>
    print(summation())
TypeError: summation() missing 2 required positional arguments: 'lower' and 'upper'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter the lower bound: 1
Enter the upper bound: 10
Enter the step value: 1
Enter the function: math.sqrt
55
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter the lower bound: 1
Enter the upper bound: 10
Enter the step value: 2
Enter the function: math.sqrt
55
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Enter the lower bound: 1
Enter the upper bound: 10
Enter the step value: 1
Enter the function: math.sqrt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 48, in <module>
    print(summation(lower, upper, step, func))
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 46, in summation
    return sum(map(func, range(lower, upper+1, step)))
TypeError: 'str' object is not callable
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 43, in <module>
    print(summation(lower, upper, step, func))
NameError: name 'lower' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200508 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200508 (file).py", line 43, in <module>
    print(summation(lower, upper, step, func))
NameError: name 'lower' is not defined
>>> def summation(lower, upper, step = 1, func = lambda x: x):
    return sum(map(func, range(lower, upper+1, step)))

print(summation(lower, upper, step, func))
SyntaxError: invalid syntax
>>> def summation(lower, upper, step = 1, func = lambda x: x):
    return sum(map(func, range(lower, upper+1, step)))

>>> 
>>> summation(1,10)
55
>>> summation(1,5)
15
>>> summation(1,10,2)
25
>>> math.sqrt
<built-in function sqrt>
>>> summation(1,10,2,math.sqrt)
10.613870096133258
>>> 