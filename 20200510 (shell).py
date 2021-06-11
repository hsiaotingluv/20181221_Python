Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ========
>>> ord('a')
97
>>> ord('1')
49
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items: []
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 99, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 96, in main
    isSorted = input("Enter a list of sorted items: ")
KeyboardInterrupt
>>> "a" > "b"
False
>>> "a" < "b"
True
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items: ["a", "b", "c"]
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items: ["a", "b", "c"]
False
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items: ["a", "b", "c"]
hello
False
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items: 2
0
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 101, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 99, in main
    print(check(isSorted))
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 92, in check
    if isSorted[i] > isSorted[i + 1]:
IndexError: string index out of range
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items: ["a", "b", "c"]
0
hello
False
>>> list = ["a", "b", "c"]
>>> list[0] > list[1]
False
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items: ["a", "b", "c"]
0
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
11
12
13
14
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 101, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 99, in main
    print(check(isSorted))
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 92, in check
    if isSorted[i] > isSorted[i + 1] == True:
IndexError: string index out of range
>>> len(list))
SyntaxError: unmatched ')'
>>> len(list)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    len(list)
TypeError: object of type 'type' has no len()
>>> list
<class 'list'>
>>> list = ["a", "b", "c"]
>>> len(list)
3
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items: ["a", "b", "c"]
0
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
11
12
13
14
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 103, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 101, in main
    print(check(isSorted))
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 92, in check
    if isSorted[i] > isSorted[i + 1] == True:
IndexError: string index out of range
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items: ["a", "b", "c"]
0
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
11
12
13
14
True
>>> 
Enter a list of sorted items: len(isSorted)
13
0
13
1
13
2
13
3
13
4
13
5
13
6
13
7
13
8
13
9
13
10
13
11
13
12
True
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items: ["a", "b", "c"]
15
0
15
1
15
2
15
3
15
4
15
5
15
6
15
7
15
8
15
9
15
10
15
11
15
12
15
13
15
14
True
>>> list = ["a", "b", "c"]
>>> len(list)
3
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
3
0
3
1
3
2
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 105, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 103, in main
    print(check(isSorted))
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 94, in check
    if isSorted[i] > isSorted[i + 1]:
IndexError: list index out of range
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
0
1
2
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 104, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 102, in main
    print(check(isSorted))
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 93, in check
    if isSorted[i] > isSorted[i + 1]:
IndexError: list index out of range
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
1
2
True
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
1
2
3
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 104, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 102, in main
    print(check(isSorted))
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 93, in check
    if isSorted[i - 1] > isSorted[i]:
IndexError: list index out of range
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
0
hello
False
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
1
2
True
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
1
2
False
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
1
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 102, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 100, in main
    print(check(isSorted))
  File "/Users/hsiaotingluv/Desktop/python/20200510 (file).py", line 93, in check
    if isSorted[i - 1] > isSorted[i]:
TypeError: '>' not supported between instances of 'str' and 'int'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
1
False
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items: a,b,c
1
2
True
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items or 'enter' to quit: a,b,c
1
2
True
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items or 'enter' to quit: a,b,c
1
2
True
Enter a list of sorted items or 'enter' to quit: 
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200510 (file).py ===========
Enter a list of sorted items or 'enter' to quit: a,2,d
False
Enter a list of sorted items or 'enter' to quit: 1,2,3
True
Enter a list of sorted items or 'enter' to quit: 14,6,3
False
Enter a list of sorted items or 'enter' to quit: 