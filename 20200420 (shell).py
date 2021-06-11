Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ord('a') - ord('c')
-2
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code text: hello
Enter the distance value: 10
xubbe
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code text: vllyon
Enter the distance value: 10
lbboed
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter a one-word, lowercase message: hello me
Enter the distance value: 10
rovvy*wo
Enter the code text: rovvy*wo
Enter the distance value: 10
hello:me
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter a one-word, lowercase message: hello me
Enter the distance value: 10
rovvy*wo
Enter the code text: rovvy*wo
Enter the distance value: 10
hello¦me
>>> ord(" ")
32
>>> chr("22")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    chr("22")
TypeError: an integer is required (got type str)
>>> chr(22)
'\x16'
>>> chr(42)
'*'
>>> chr(42-10)
' '
>>> ord('a') - ord('*')
55
>>> ord('a')
97
>>> ord('z')
122
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter a one-word, lowercase message: helllo me
Enter the distance value: 10
rovvvy*wo
Enter the code text: rovvvy*wo
Enter the distance value: 10
helllo:me
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter a one-word, lowercase message: e
Enter the distance value: 10
o
Enter the code text: rovvvy wo
Enter the distance value: 10
hellloome
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter a one-word, lowercase message: d
Enter the distance value: 1
e
Enter the code text: rovvvy wo
Enter the distance value: 10
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200418 (file).py", line 37, in <module>
    if cipherValue < ord('a'):
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter a one-word, lowercase message: hello world
Enter the distance value: 10
rovvy*gybvn
Enter the code text: rovvy gybvn
Enter the distance value: 10
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200418 (file).py", line 36, in <module>
    if cipherValue < ord('a'):
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter a one-word, lowercase message: 1
Enter the distance value: d
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200418 (file).py", line 8, in <module>
    distance = int(input("Enter the distance value: "))
ValueError: invalid literal for int() with base 10: 'd'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter a one-word, lowercase message: hello world
Enter the distance value: 10
rovvy*gybvn
Enter the code text: rovvy gybvn
Enter the distance value: 10
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200418 (file).py", line 40, in <module>
    plainText += chr(cipherValue)
TypeError: an integer is required (got type str)
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter a one-word, lowercase message: hello world
Enter the distance value: 10
rovvy*gybvn
Enter the code text: rovvy gybvn
Enter the distance value: 10
hello world
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter a one-word, lowercase message: hello world my name is hsiao ting
Enter the distance value: 10
rovvy*gybvn*wi*xkwo*sc*rcsky*dsxq
Enter the code text: rovvy*gybvn*wi*xkwo*sc*rcsky*dsxq
Enter the distance value: 10
hello*world*my*name*is*hsiao*ting
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hello world! My name is hsiao ting
rovvy gybvn! wi xkwo sc rcsky dsxq

Enter the code to decrypt: rovvy gybvn! wi xkwo sc rcsky dsxq
26 rovvy gybvn! wi xkwo sc rcsky dsxq
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to decrypt: rovvy gybvn! wi xkwo sc rcsky dsxq
26 rovvy gybvn! wi xkwo sc rcsky dsxq
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to decrypt: rovvy gybvn! wi xkwo sc rcsky dsxq
1 qnuux fxaum! vh wjvn rb qbrjx crwp
2 pmttw ewztl! ug vium qa paqiw bqvo
3 olssv dvysk! tf uhtl pz ozphv apun
4 nkrru cuxrj! se tgsk oy nyogu zotm
5 mjqqt btwqi! rd sfrj nx mxnft ynsl
6 lipps asvph! qc reqi mw lwmes xmrk
7 khoor zruog! pb qdph lv kvldr wlqj
8 jgnnq yqtnf! oa pcog ku jukcq vkpi
9 ifmmp xpsme! nz obnf jt itjbp ujoh
10 hello world! my name is hsiao ting
11 gdkkn vnqkc! lx mzld hr grhzn shmf
12 fcjjm umpjb! kw lykc gq fqgym rgle
13 ebiil tloia! jv kxjb fp epfxl qfkd
14 dahhk sknhz! iu jwia eo doewk pejc
15 czggj rjmgy! ht ivhz dn cndvj odib
16 byffi qilfx! gs hugy cm bmcui ncha
17 axeeh phkew! fr gtfx bl albth mbgz
18 zwddg ogjdv! eq fsew ak zkasg lafy
19 yvccf nficu! dp erdv zj yjzrf kzex
20 xubbe mehbt! co dqcu yi xiyqe jydw
21 wtaad ldgas! bn cpbt xh whxpd ixcv
22 vszzc kcfzr! am boas wg vgwoc hwbu
23 uryyb jbeyq! zl anzr vf ufvnb gvat
24 tqxxa iadxp! yk zmyq ue teuma fuzs
25 spwwz hzcwo! xj ylxp td sdtlz etyr
26 rovvy gybvn! wi xkwo sc rcsky dsxq
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter to encrypt: hello world
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter to encrypt: hello world! My name is hsiao ting
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 20, in <module>
    code += cipherValue
TypeError: can only concatenate str (not "int") to str
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter to encrypt: hello world! My name is hsiao ting
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter to encrypt: hello world! My name is hsiao ting
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 42, in <module>
    translated += chr(cipherValue)
NameError: name 'translated' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter to encrypt: hello world! My name is hsiao ting
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter to encrypt: hello world! My name is hsiao ting
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter to encrypt: hello world! My name is hsiao ting
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter to encrypt: hello world! My name is hsiao ting
>>> num = 1
>>> decimal = 10
>>> oct(decimal)
'0o12'
>>> decimal % 8
2
>>> decimal / 8
1.25
>>> 1 / 8
0.125
>>> 9 / 8
1.125
>>> decimal = 1.102
>>> decimal
1.102
>>> oct(decimal)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    oct(decimal)
TypeError: 'float' object cannot be interpreted as an integer
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal integer: 12
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 55, in <module>
    print("The octal number is", decimalToOctal(decimal))
NameError: name 'decimalToOctal' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal integer: 12
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 55, in <module>
    print("The octal number is", decimalToOctal(decimal))
NameError: name 'decimalToOctal' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal integer: 12
The octal number is None
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal integer: 12
The octal number is 12
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal integer: 10
The octal number is 10
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal integer: 12
The octal number is 14
>>> int(12/8)
1
>>> 12 % 8
4
>>> 112 % 8
0
>>> 112 / 8
14.0
>>> 14 % 10
4
>>> 1 % 10
1
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
choose to convert octal to decimal or vise versa: octal to decimal
Enter an octal integer: 134
The decimal number is 92
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
choose to convert octal to decimal or vise versa: decimal to octal
Enter a decimal integer: 92
The octal number is 134
>>> def function()
SyntaxError: invalid syntax
>>> def function(x, y):
	return x + y

>>> function(1, 2)
3
>>> function(x):
	
SyntaxError: invalid syntax
>>> def function(x):
	print(x)
	print("still this function")

	
>>> function(4)
4
still this function
>>> function(f)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    function(f)
NameError: name 'f' is not defined
>>> x = 1011
>>> x.split()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x.split()
AttributeError: 'int' object has no attribute 'split'
>>> x.strip()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    x.strip()
AttributeError: 'int' object has no attribute 'strip'
>>> x = "1011"
>>> x.split()
['1011']
>>> x.split(1)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    x.split(1)
TypeError: must be str or None, not int
>>> x.split("0")
['1', '11']
>>> x.split("1")
['', '0', '', '']
>>> x.rpartition()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    x.rpartition()
TypeError: rpartition() takes exactly one argument (0 given)
>>> x.rpartition("1")
('101', '1', '')
>>> x.join(3)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x.join(3)
TypeError: can only join an iterable
>>> x.join("1")
'1'
>>> x
'1011'
>>> x.del("1")
SyntaxError: invalid syntax
>>> x[:]
'1011'
>>> x[1:]
'011'
>>> x[:1]
'1'
>>> x[1:] + x[:1]
'0111'
>>> x
'1011'
>>> x[:1] + x[:3]
'1101'
>>> x[:3]
'101'
>>> x
'1011'
>>> x[1:]
'011'
>>> x[:1] + x[1:]
'1011'
>>> x = "1234"
>>> x
'1234'
>>> x[:1]
'1'
>>> x[:3]
'123'
>>> x[:-1]
'123'
>>> x[-1:]
'4'
>>> x[1:]
'234'
>>> x[1:] + x[:1]
'2341'
>>> x[-1:] + x[:-1]
'4123'
>>> x = "1234567890"
>>> x[1:] + x[:1]
'2345678901'
>>> x[-1:] + x[:-1]
'0123456789'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a bit string: 101101011
Enter to shiftLeft or shiftRight: shiftLeft
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 88, in <module>
    print("The shifted bits is:", shiftLeft(bitString))
NameError: name 'shiftLeft' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
>>> heelo
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    heelo
NameError: name 'heelo' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
>>> s
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
>>> hsiaoting
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    hsiaoting
NameError: name 'hsiaoting' is not defined
>>> set("aeiou").intersection
<built-in method intersection of set object at 0x10ff3ee40>
>>> set("aeiou").intersec
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    set("aeiou").intersec
AttributeError: 'set' object has no attribute 'intersec'
>>> name = "hsiaoting"
>>> set("aeiou").intersection(name)
{'i', 'o', 'a'}
>>> set("hsiao").intersection(name)
{'i', 'h', 'o', 'a', 's'}
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter your name: hsiaoting
Your name contains a vowel.
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
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a bit string: 1010011
Enter to shiftLeft or shiftRight: shiftLeft
The shifted bits is: 0100111
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a bit string: 1235624
Enter to shiftLeft or shiftRight: shiftRight
The shifted bits is: 4123562
>>> ord(1)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    ord(1)
TypeError: ord() expected string of length 1, but int found
>>> ord("1")
49
>>> chr(50)
'2'
>>> x
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x = "123"
>>> x += "123" + "123"
>>> x
'123123123'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 12
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 123, in <module>
    for num in decimal:
TypeError: 'int' object is not iterable
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 12
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 130, in <module>
    bitString += (decimal % 2) * i
TypeError: not all arguments converted during string formatting
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 12
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 132, in <module>
    i = i * 10
KeyboardInterrupt







>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 12
6
3
1
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 132, in <module>
    print(decimal)
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 12
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 134, in <module>
    bitString = bitString[1:] + bitString[:1]
TypeError: 'int' object is not subscriptable
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 12
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 134, in <module>
    bitString = str(bitString[1:]) + str(bitString[:1])
TypeError: 'int' object is not subscriptable
>>> x = 12
>>> str(x[1:])
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    str(x[1:])
TypeError: 'int' object is not subscriptable
>>> str(x)
'12'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 12
The encrypted string is 100101 100111 
>>> ord(1)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    ord(1)
TypeError: ord() expected string of length 1, but int found
>>> ord("1")
49
>>> x = 100101 100111
SyntaxError: invalid syntax
>>> x = "100101 100111"
>>> x.split(" ")
['100101', '100111']
>>> for num in x:
	print(x)

	
100101 100111
100101 100111
100101 100111
100101 100111
100101 100111
100101 100111
100101 100111
100101 100111
100101 100111
100101 100111
100101 100111
100101 100111
100101 100111
>>> x
'100101 100111'
>>> x = x.split(" ")
>>> x
['100101', '100111']
>>> for num in x:
	print(x)

	
['100101', '100111']
['100101', '100111']
>>> for num in x:
	print(num)

	
100101
100111
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 12
The encrypted string is 100101 100111 
Enter a code to decrypt: 100101 100111
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 155, in <module>
    num = chr(cipherValue) - 1
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 100101 100111
The encrypted string is 100101 100011 100011 100101 100011 100101 000011 100101 100011 100011 100101 100101 100101 
Enter a code to decrypt: 100101 100111
The decrypted decimal is &
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 100101 100111
The encrypted string is 100101 100011 100011 100101 100011 100101 000011 100101 100011 100011 100101 100101 100101 
Enter a code to decrypt: 100101 100111
100101
100111
The decrypted decimal is &
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 120, in <module>
    decimal = input("Enter a decimal to encrypt: ")
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a code to decrypt: 100101 100111
100101
100101
100111
100111
The decrypted decimal is &
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a code to decrypt: 100101 100111
100101
100111
The decrypted decimal is 2
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a code to decrypt: 100101 100111
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 158, in <module>
    num += chr(num)
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a code to decrypt: 100101 100111
The decrypted decimal is 12
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 1234
The encrypted string is 100101 100111 101001 101011 
Enter a code to decrypt: 100101 100111 101001 101011 
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 147, in <module>
    shiftRight = int(shiftRight)
ValueError: invalid literal for int() with base 10: ''
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 1234
The encrypted string is 100101 100111 101001 101011 
Enter a code to decrypt: 100101 100111 101001 101011 
110010
110011
110100
110101

Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 148, in <module>
    shiftRight = int(shiftRight)
ValueError: invalid literal for int() with base 10: ''
>>> int('5.0')
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    int('5.0')
ValueError: invalid literal for int() with base 10: '5.0'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 1234
The encrypted string is 100101 100111 101001 101011 
Enter a code to decrypt: 100101 100111 101001 101011 
110010
110011
110100
110101

Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 148, in <module>
    shiftRight = int(float(shiftRight))
ValueError: could not convert string to float: ''
>>> x = "100101 100111 101001 101011 "
>>> x = "100101"
>>> int(x,2)
37
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 1234
The encrypted string is 100101 100111 101001 101011 
Enter a code to decrypt: 100101 100111 101001 101011 
110010
110011
110100
110101

Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 148, in <module>
    shiftRight = int(shiftRight, 2)
ValueError: invalid literal for int() with base 2: ''
>>> int("1")
1
>>> int("1010101")
1010101
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 1234
The encrypted string is 100101 100111 101001 101011 
Enter a code to decrypt: 100101 100111 101001 101011 
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 147, in <module>
    shiftRight = int(shiftRight)
ValueError: invalid literal for int() with base 10: ''
>>> x = "1234"
>>> x = int(x)
>>> x
1234
>>> shiftRight = "100101"
>>> shiftRight = int(shiftRight)
>>> shiftRight
100101
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 1234
The encrypted string is 100101 100111 101001 101011 
Enter a code to decrypt: 100101 100111 101001 101011
The decrypted decimal is 1234
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 1234123
The encrypted string is 100101 100111 101001 101011 100101 100111 101001 
Enter a code to decrypt: 100101 100111 101001 101011 100101 100111 101001
The decrypted decimal is 1234123
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: o3
The encrypted string is 1100001 101001 
Enter a code to decrypt: 1100001 101001
The decrypted decimal is o3
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: Hello world, my name is hsiaoting. I am 20 this year
The encrypted string is 0010011 1001101 1011011 1011011 1100001 000011 1110001 1100001 1100111 1011011 1001011 011011 000011 1011101 1110101 000011 1011111 1000101 1011101 1001101 000011 1010101 1101001 000011 1010011 1101001 1010101 1000101 1100001 1101011 1010101 1011111 1010001 011111 000011 0010101 000011 1000101 1011101 000011 100111 100011 000011 1101011 1010011 1010101 1101001 000011 1110101 1001101 1000101 1100111 
Enter a code to decrypt: 0010011 1001101 1011011 1011011 1100001 000011 1110001 1100001 1100111 1011011 1001011 011011 000011 1011101 1110101 000011 1011111 1000101 1011101 1001101 000011 1010101 1101001 000011 1010011 1101001 1010101 1000101 1100001 1101011 1010101 1011111 1010001 011111 000011 0010101 000011 1000101 1011101 000011 100111 100011 000011 1101011 1010011 1010101 1101001 000011 1110101 1001101 1000101 1100111 
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 147, in <module>
    shiftRight = int(float(shiftRight))
ValueError: could not convert string to float: ''
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter a decimal to encrypt: 128395072017401
The encrypted string is 100101 100111 110011 101001 110101 101101 100011 110001 100111 100011 100101 110001 101011 100011 100101 
Enter a code to decrypt: 100101 100111 110011 101001 110101 101101 100011 110001 100111 100011 100101 110001 101011 100011 100101
The decrypted decimal is 128395072017401
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 173, in <module>
    f2.write("\n", "The copied text file", "\n")
TypeError: write() takes exactly one argument (3 given)
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 194, in <module>
    f2.write(count, line)
TypeError: write() takes exactly one argument (2 given)
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 196, in <module>
    f2.write()
TypeError: write() takes exactly one argument (0 given)
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> print("%4d%10s" % (count, line))
  67         .
>>> count
67
>>> count = 1
>>> line = hsiaoting
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    line = hsiaoting
NameError: name 'hsiaoting' is not defined
>>> line = "hsiaoting"
>>> print("%4d%10s" % (count, line))
   1 hsiaoting
>>> print("%4-d%10s" % (count, line))
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    print("%4-d%10s" % (count, line))
ValueError: unsupported format character '-' (0x2d) at index 2
>>> print("%d%4s" % (count, line))
1hsiaoting
>>> print("%d%20s" % (count, line))
1           hsiaoting
>>> print("%d%-4s" % (count, line))
1hsiaoting
>>> print("%d%-20s" % (count, line))
1hsiaoting           
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 195, in <module>
    f2.write(count + ")   " + line + "\n")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 195, in <module>
    f2.write(count, ")   ", line, "\n")
TypeError: write() takes exactly one argument (4 given)
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
helloH
helloe
hellol
hellol
helloo
hello 
hellow
helloo
hellor
hellol
hellod
hello!
hello

helloM
helloy
hello 
hellon
helloa
hellom
helloe
hello 
helloi
hellos
hello 
helloh
hellos
helloi
helloa
helloo
hellot
helloi
hellon
hellog
hello~
hello

helloA
hellor
helloe
hello 
helloy
helloo
hellou
hello 
hellot
helloh
helloe
hellor
helloe
hello?
hello

helloN
helloi
helloc
helloe
hello 
hellot
helloo
hello 
hellom
helloe
helloe
hellot
hello 
helloy
helloo
hellou
hello.
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt

=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 195, in <module>
    f2.write(char)
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt

=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt

=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200420 (file).py", line 196, in <module>
    char = f1.readline()
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/codecs.py", line 319, in decode
    def decode(self, input, final=False):
KeyboardInterrupt

>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
Hello world!
My name is hsiaoting~
Are you there?
Nice to meet you.
>>> x
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x = "hsiaoting"
>>> x.rjust(4, "   ")
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    x.rjust(4, "   ")
TypeError: The fill character must be exactly one character long
>>> x.rjust(4)
'hsiaoting'
>>> x.rjust(4, " ")
'hsiaoting'
>>> x.rjust(10, " ")
' hsiaoting'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
Hello world!
My name is hsiaoting~
Are you there?
Nice to meet you.
>>> x.ljust(4, " ")
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    x.ljust(4, " ")
NameError: name 'x' is not defined
>>> x = "hsiaoting"
>>> x.ljust(4, " ")
'hsiaoting'
>>> print("%4s%4s" % ("1", ">"))
   1   >
>>> print("%s%4s" % ("1", ">"))
1   >
>>> print("%s%-4s" % ("1", ">"))
1>   
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200420 (file).py ===========
Enter the file to copy: test.txt
Enter the file to paste into: test1.txt
>>> 