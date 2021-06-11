Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> temp = input("不妨猜一下小甲鱼现在心理想的是哪个数字。")
guess = int(temp)

if guess == 8:
    print("你是小甲鱼心里的蛔虫嘛？！")
    print("哼，猜中了也没奖励！"
else:
    print("猜错啦，小甲鱼现在心里想的是8！")
    
print("游戏结束，不玩啦^_^")

SyntaxError: multiple statements found while compiling a single statement
>>> dir(_builtins_)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    dir(_builtins_)
NameError: name '_builtins_' is not defined
>>> x = 3
>>> x
3
>>> print(x)
3
>>> 
>>> loveyou1314 = 1314
>>> 520baby = 520
SyntaxError: invalid syntax
>>> 幸运数 = 588
>>> print(幸运数)
588
>>> name = "小甲鱼"
>>> print(name)
小甲鱼
>>> z = 2
>>> x = 1
>>> y = 5
>>> print(x+y+z)
8
>>> print(x*y + z*y)
15
>>> print(x/y)
0.2
>>> print('I love you')
I love you
>>> print("\"I love you, let\'s go out\"")
"I love you, let's go out"
>>> print("I love Python.\nI love FishC.")
I love Python.
I love FishC.
>>> print("I love Python. \n I love FishC.")
I love Python. 
 I love FishC.
>>> print("D:\\three\\two\\one\\now")
D:\three\two\one\now
>>> print("\t")
	
>>> print("\td")
	d
>>> print(r"I love Python.\nI love FishC.")
I love Python.\nI love FishC.
>>> print(r"\"I love you, let\'s go out\"")
\"I love you, let\'s go out\"
>>> print("\"I love you, let\'s go out\"")
"I love you, let's go out"
>>> print(r""I love you, let's go out"")
      
SyntaxError: invalid syntax
>>> print(r"\"I love you, let's go out"")

SyntaxError: EOL while scanning string literal
>>> print(r"\"I love you, let's go out"")
      
SyntaxError: EOL while scanning string literal
>>> print(r"\"I love you, let's go out\"")
\"I love you, let's go out\"
>>> 
>>> print(r"I love you, let's go out")
I love you, let's go out
>>> print(r""I love you, let's go out"")
      
SyntaxError: invalid syntax
>>> print(r"\"I love you, let's go out\"")
\"I love you, let's go out\"
>>> print(r""I love you, let's go out"")
      
SyntaxError: invalid syntax
>>> print(r"\"I love you, let's go out"\")
SyntaxError: unexpected character after line continuation character
>>> print("        \n\")
      
SyntaxError: EOL while scanning string literal
>>> print("            \n\
         @             \n\
        / \\           \n\
        * *            \n\
        * *            \n\
        * *            \n\
    * * * * * *        \n\
  * * * * * * * *      \n\
* * * * * * * * * *    \n\
        * *            \n\
        * *            \n\
      * * * *          \n\
    * * * * * *\n\n\n")
            
         @             
        / \           
        * *            
        * *            
        * *            
    * * * * * *        
  * * * * * * * *      
* * * * * * * * * *    
        * *            
        * *            
      * * * *          
    * * * * * *



>>> print("            \n
         @             \n\
        / \\           \n\
        * *            \n\
        * *            \n\
        * *            \n\
    * * * * * *        \n\
  * * * * * * * *      \n\
* * * * * * * * * *    \n\
        * *            \n\
        * *            \n\
      * * * *          \n\
    * * * * * *\n\n\n")
      
SyntaxError: EOL while scanning string literal
>>> print("            \n\
         @             \n\
        / \\           \n\
        * *            \n\
        * *            \n\
        * *            \n\
    * * * * * *        \n\
  * * * * * * * *      \n\
* * * * * * * * * *    \n\
        * *            \n\
        * *            \n\
      * * * *          \n\
    * * * * * *\n\n\")
      
SyntaxError: EOL while scanning string literal
>>> print("            \n\
         @             \n\
        / \\           \n\
        * *            \n\
        * *            \n\
        * *            \n\
    * * * * * *        \n\
  * * * * * * * *      \n\
* * * * * * * * * *    \n\
        * *            \n\
        * *            \n\
      * * * *          \n\
    * * * * * *\n\n")
            
         @             
        / \           
        * *            
        * *            
        * *            
    * * * * * *        
  * * * * * * * *      
* * * * * * * * * *    
        * *            
        * *            
      * * * *          
    * * * * * *


>>> print("            \n\
         @             \n\
        / \\           \n\
        * *            \n\
        * *            \n\
        * *            \n\
    * * * * * *        \n\
  * * * * * * * *      \n\
* * * * * * * * * *    \n\
        * *            \n\
        * *            \n\
      * * * *          \n\
    * * * * * *\n")
            
         @             
        / \           
        * *            
        * *            
        * *            
    * * * * * *        
  * * * * * * * *      
* * * * * * * * * *    
        * *            
        * *            
      * * * *          
    * * * * * *

>>> print("            \n\
         @             \n\
        / \\           \n\
        * *            \n\
        * *            \n\
        * *            \n\
    * * * * * *        \n\
  * * * * * * * *      \n\
* * * * * * * * * *    \n\
        * *            \n\
        * *            \n\
      * * * *          \n\
    * * * * * *")
            
         @             
        / \           
        * *            
        * *            
        * *            
    * * * * * *        
  * * * * * * * *      
* * * * * * * * * *    
        * *            
        * *            
      * * * *          
    * * * * * *
>>> print("            \n\
         @             \n\
        / \\           \n\
        * *            \n\
        * *            \n\
        * *            \n\
    * * * * * *        \n\
  * * * * * * * *      \n\
* * * * * * * * * *    \n\
        * *            \n
        * *            \n\
      * * * *          \n\
    * * * * * *\n\n\n")
      
SyntaxError: EOL while scanning string literal
>>> print("            \n\
         @             \n\
        / \\           \n\
        * *            \n\
        * *            \n\
        * *            \n\
    * * * * * *        \n\
  * * * * * * * *      \n\
* * * * * * * * * *    \n\
        * *            \n\
        * *            \n\
      * * * *          \n\
    * * * * * *\n\n\n")
            
         @             
        / \           
        * *            
        * *            
        * *            
    * * * * * *        
  * * * * * * * *      
* * * * * * * * * *    
        * *            
        * *            
      * * * *          
    * * * * * *



>>> print("            \n\
         @             \n\
        / \\           \n\
        * *            \n\
        * *            \n\
        * *            \n\
    * * * * * *        \n\
  * * * * * * * *      \n\
* * * * * * * * * *    \n\
        * *            \n\
        * *            \n\
      * * * *          \n\
    * * * * * *\n\n\n\")
      
SyntaxError: EOL while scanning string literal
>>> print("n\
         @             \n\
        / \\           \n\
        * *            \n\
        * *            \n\
        * *            \n\
    * * * * * *        \n\
  * * * * * * * *      \n\
* * * * * * * * * *    \n\
        * *            \n\
        * *            \n\
      * * * *          \n\
    * * * * * *\n\n\n")
n         @             
        / \           
        * *            
        * *            
        * *            
    * * * * * *        
  * * * * * * * *      
* * * * * * * * * *    
        * *            
        * *            
      * * * *          
    * * * * * *



>>> print("            n\
         @             \n\
        / \\           \n\
        * *            \n\
        * *            \n\
        * *            \n\
    * * * * * *        \n\
  * * * * * * * *      \n\
* * * * * * * * * *    \n\
        * *            \n\
        * *            \n\
      * * * *          \n\
    * * * * * *\n\n\n")
            n         @             
        / \           
        * *            
        * *            
        * *            
    * * * * * *        
  * * * * * * * *      
* * * * * * * * * *    
        * *            
        * *            
      * * * *          
    * * * * * *



>>> print("""
	youyouyouyouyou
	fhowfi
	faoihomx
	ioxfoi
	aoijf oaj
	ao hooiem
	aoihoijj
	joa
	""")

	youyouyouyouyou
	fhowfi
	faoihomx
	ioxfoi
	aoijf oaj
	ao hooiem
	aoihoijj
	joa
	
>>> print("
	youyouyouyouyou
	fhowfi
	faoihomx
	ioxfoi
	aoijf oaj
	ao hooiem
	aoihoijj
	joa")
      
SyntaxError: EOL while scanning string literal
>>> print('
      
SyntaxError: EOL while scanning string literal
>>> poetry = """
	youyouyouyouyou
	fhowfi
	faoihomx
	ioxfoi
	aoijf oaj
	ao hooiem
	aoihoijj
	joa
	"""
>>> print(poetry)

	youyouyouyouyou
	fhowfi
	faoihomx
	ioxfoi
	aoijf oaj
	ao hooiem
	aoihoijj
	joa
	
>>> poetry = """youyouyouyouyou
	fhowfi
	faoihomx
	ioxfoi
	aoijf oaj
	ao hooiem
	aoihoijj
	joa"""
>>> print(poetry)
youyouyouyouyou
	fhowfi
	faoihomx
	ioxfoi
	aoijf oaj
	ao hooiem
	aoihoijj
	joa
>>> poetry =
	"""youyouyouyouyou
	fhowfi
	faoihomx
	ioxfoi
	aoijf oaj
	ao hooiem
	aoihoijj
	joa"""
	
SyntaxError: invalid syntax
>>>  poetry = """youyouyouyouyou
	fhowfi
	faoihomx
	ioxfoi
	aoijf oaj
	ao hooiem
	aoihoijj
	joa"""
 
SyntaxError: unexpected indent
>>>  poetry ="""	youyouyouyouyou
	fhowfi
	faoihomx
	ioxfoi
	aoijf oaj
	ao hooiem
	aoihoijj
	joa"""
 
SyntaxError: unexpected indent
>>> poetry ="""	youyouyouyouyou
	fhowfi
	faoihomx
	ioxfoi
	aoijf oaj
	ao hooiem
	aoihoijj
	joa"""
>>> print(poetry)
	youyouyouyouyou
	fhowfi
	faoihomx
	ioxfoi
	aoijf oaj
	ao hooiem
	aoihoijj
	joa
>>> temp = input("你是谁：")
你是谁：我是你爸爸
>>> temp
'我是你爸爸'
>>> print(temp)
我是你爸爸
>>> print(int(temp))
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    print(int(temp))
ValueError: invalid literal for int() with base 10: '我是你爸爸'
>>> temp = int("你几岁:")
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    temp = int("你几岁:")
ValueError: invalid literal for int() with base 10: '你几岁:'
>>> temp = input(int"你几岁:")
SyntaxError: invalid syntax
>>> temp = input("你几岁：")
你几岁：8
>>> print(temp)
8
>>> print(temp + 8)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print(temp + 8)
TypeError: can only concatenate str (not "int") to str
>>> guess = int(temp)
>>> print(guess + 8)
16
>>> temp = input("你几岁：")
你几岁：fe
>>> temp = int(input"你几岁：")
SyntaxError: invalid syntax
>>> temp = input(int"你几岁：")
SyntaxError: invalid syntax
>>> temp = input("你几岁：")
你几岁：
>>> 
>>> 3 = 2
SyntaxError: cannot assign to literal
>>> 3 = 4
SyntaxError: cannot assign to literal
>>> 3 = 3
SyntaxError: cannot assign to literal
>>> 3 == 4
False
>>> 4 != r
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    4 != r
NameError: name 'r' is not defined
>>> 2 != 5
True
>>> 2 =! 5
SyntaxError: invalid syntax
>>> 
== RESTART: /Users/hsiaotingluv/Documents/game.py ==
不妨猜一下小甲鱼现在心理想的是哪个数字。8
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
不妨猜一下小甲鱼现在心理想的是哪个数字。
== RESTART: /Users/hsiaotingluv/Documents/game.py ==
不妨猜一下小甲鱼现在心理想的是哪个数字:8
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
不妨猜一下小甲鱼现在心理想的是哪个数字:8
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
不妨猜一下小甲鱼现在心理想的是哪个数字:8
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
游戏结束，不玩啦^_^
>>> 
== RESTART: /Users/hsiaotingluv/Documents/game.py ==
不妨猜一下小甲鱼现在心理想的是哪个数字:8
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
不妨猜一下小甲鱼现在心理想的是哪个数字:8
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
不妨猜一下小甲鱼现在心理想的是哪个数字:8
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
不妨猜一下小甲鱼现在心理想的是哪个数字:8
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
不妨猜一下小甲鱼现在心理想的是哪个数字:8
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
不妨猜一下小甲鱼现在心理想的是哪个数字:8
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
不妨猜一下小甲鱼现在心理想的是哪个数字:8
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
不妨猜一下小甲鱼现在心理想的是哪个数字:
== RESTART: /Users/hsiaotingluv/Documents/game.py ==
不妨猜一下小甲鱼现在心理想的是哪个数字:
== RESTART: /Users/hsiaotingluv/Documents/game.py ==
不妨猜一下小甲鱼现在心理想的是哪个数字:8
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
游戏结束，不玩啦^_^
>>> import random
>>> random
<module 'random' from '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/random.py'>
>>> random.randint(1,10)
9
>>> random.randint(1,10,9)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    random.randint(1,10,9)
TypeError: randint() takes 3 positional arguments but 4 were given
>>> random.randint(122,10111)
3417
>>> random.randint(1.0,10)
2
>>> random.randint(1,10,12)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    random.randint(1,10,12)
TypeError: randint() takes 3 positional arguments but 4 were given
>>> random.randint(1,2)
1
>>> 
====== RESTART: /Users/hsiaotingluv/Documents/game.py ======
不妨猜一下小甲鱼现在心理想的是哪个数字:8
大啦～
不妨猜一下小甲鱼现在心理想的是哪个数字:8
大啦～
不妨猜一下小甲鱼现在心理想的是哪个数字:8
大啦～
游戏结束，不玩啦^_^
>>> 
====== RESTART: /Users/hsiaotingluv/Documents/game.py ======
不妨猜一下小甲鱼现在心理想的是哪个数字:4
小啦～
不妨猜一下小甲鱼现在心理想的是哪个数字:7
小啦～
不妨猜一下小甲鱼现在心理想的是哪个数字:8
大啦～
游戏结束，不玩啦^_^
>>> 
====== RESTART: /Users/hsiaotingluv/Documents/game.py ======
不妨猜一下小甲鱼现在心理想的是哪个数字:8
大啦～
不妨猜一下小甲鱼现在心理想的是哪个数字:5
小啦～
不妨猜一下小甲鱼现在心理想的是哪个数字:6
小啦～
游戏结束，不玩啦^_^
>>> 
====== RESTART: /Users/hsiaotingluv/Documents/game.py ======
不妨猜一下小甲鱼现在心理想的是哪个数字:6
小啦～
不妨猜一下小甲鱼现在心理想的是哪个数字:8
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
游戏结束，不玩啦^_^
>>> 
====== RESTART: /Users/hsiaotingluv/Documents/game.py ======
不妨猜一下小甲鱼现在心理想的是哪个数字:8
大啦～
不妨猜一下小甲鱼现在心理想的是哪个数字:6
大啦～
不妨猜一下小甲鱼现在心理想的是哪个数字:3
大啦～
游戏结束，不玩啦^_^
>>> 
====== RESTART: /Users/hsiaotingluv/Documents/game.py ======
不妨猜一下小甲鱼现在心理想的是哪个数字:5
大啦～
不妨猜一下小甲鱼现在心理想的是哪个数字:3
你是小甲鱼心里的蛔虫嘛？！
哼，猜中了也没奖励！
游戏结束，不玩啦^_^
>>> x = random.getstate()
>>> print(x)

>>> random.randint(1,10)
10
>>> random.randint(1,10)
4
>>> random.randint(1,10)
4
>>> random.randint(1,10)
10
>>> random.randint(1,10)
7
random.randint(1,10)
>>> 
>>> random.randint(1,10)
7
>>> random.randint(1,10)
4
>>> random.randint(1,10)
6
>>> random.randint(1,10)
9
>>> random.randint(1,10)
2
>>> random.randint(1,10)
4
>>> random.randint(1,10)
2
>>> random.setstate(x)
>>> random.randint(1,10)
10
>>> random.randint(1,10)
4
>>> random.randint(1,10)
4
>>> random.randint(1,10)
10
>>> random.randint(1,10)
7
>>> random.randint(1,10)
7
>>> random.randint(1,10)
4
>>> random.randint(1,10)
6
>>> 144/144
1.0
>>> 3/3
1.0
>>> float
<class 'float'>
>>> 0.1+0.2
0.30000000000000004
>>> 0.1 + 0.3
0.4
>>> i = 0
>>> while i < 1:
	i = i + 0.1
	print(i)

	
0.1
0.2
0.30000000000000004
0.4
0.5
0.6
0.7
0.7999999999999999
0.8999999999999999
0.9999999999999999
1.0999999999999999
>>> import decimal
>>> decimal.Decimal("0.1")
Decimal('0.1')
>>> a = decimal.Decimal("0.1")
>>> b = decimal.Decimal("0.2")
>>> a + b
Decimal('0.3')
>>> 0.3 == a + b
False
>>> 0.3 == int(a+b)
False
>>> c = decimal.Decimal("0.3")
>>> a + b == c
True
>>> 0.00005
5e-05
>>> 1 + 2j
(1+2j)
>>> x = 1 + 2j
>>> x.real
1.0
>>> x.imag
2.0
>>> 3 // 2
1
>>> -2 // -2
1
>>> -3 // -2
1
>>> -3 // 2
-2
>>> -5 // 2
-3
>>> 3 % 2
1
>>> 6 % 2
0
>>> -3 % 2
1
>>> 9 == (9 // 2)*2 + (9 % 2)
True
>>> divmod(3,2)
(1, 1)
>>> divmod(5,2)
(2, 1)
>>> divmod(8,2.3)
(3.0, 1.1000000000000005)
>>> x = -930.3
>>> abs(x)
930.3
>>> z = 1 + 2j
>>> abs(z)
2.23606797749979
>>> int('520')
520
>>> int(3.14)
3
>>> int('c')
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    int('c')
ValueError: invalid literal for int() with base 10: 'c'
>>> float('3.14')
3.14
>>> float(520)
520.0
>>> int(520)
520
>>> int('520')
520
>>> float('+1E6')
1000000.0
>>> complex('1+2j')
(1+2j)
>>> int('3820')
3820
>>>  pow(2,3)
 
SyntaxError: unexpected indent
>>> pow(2,3)
8
>>> 2 ** 3
8
>>> pow(2,-3)
0.125
>>> 2 ** -3
0.125
>>> pow(2,3,5)
3
>>> 2 ** 3 % 5
3
>>> 3 % 5
3
>>> 8 % 5
3
>>> bool(250)
True
>>> bool('false')
True
>>> bool(false)
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    bool(false)
NameError: name 'false' is not defined
>>> bool(False)
False
>>> bool(True)
True
>>> bool('')
False
>>> bool(" ")
True
>>> bool(03)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> bool(0.0)
False
>>> 0 == False
True
>>> 1 == True
True
>>> True + False
1
>>> True - False
1
>>> True / False
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    True / False
ZeroDivisionError: division by zero
>>> 3 < 4 and 4>5
False
>>> 3 < 4 or 4 > 5
True
>>> not True
False
>>> not False
True
>>> not 250
False
>>> not 0
True
>>> not 3 < 4 or 4 > 5
False
>>> 3 < 4 or 4 > 5
True
>>> 
>>> False or 1 or 4 or 6 or 9
1
>>> not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9
4
>>> 0 or 4
4
>>> 3 and 4
4
>>> not 1
False
>>> False or 1 or 4 or 6 or 9
1
>>> 0 and 1
0
>>> False or 0 or 4 or 6 or 9
4
>>> "s'
SyntaxError: EOL while scanning string literal
>>> 's"
SyntaxError: EOL while scanning string literal
>>> var = True
>>> var
True
>>> ord('a')
97
>>> ord("A")
65
>>> chr(65)
'A'
>>> var = "a"
>>> num = ord(var)
>>> num += 10
>>> var = chr(num)
>>> var
'k'
>>> string = "hello \n world"
>>> print(string)
hello 
 world
>>> string = 'dfa'
>>> string = "dfas"
>>> string = "Let's"
>>> string
"Let's"
>>> string = 'ldafksjd"dfasdf"fasdf'
>>> string
'ldafksjd"dfasdf"fasdf'
>>> print(string)
ldafksjd"dfasdf"fasdf
>>> print("""d;s'daf "deuigd"dee""")
d;s'daf "deuigd"dee
>>> print(r"eaihfoihod'sdijf")
eaihfoihod'sdijf
>>> \t
SyntaxError: unexpected character after line continuation character
>>> 

>>> print("dfas
      fa")
      
SyntaxError: EOL while scanning string literal
>>> print("dfas  \n\
      fa")
dfas  
      fa
>>> var = "10"
>>> var += 5
Traceback (most recent call last):
  File "<pyshell#260>", line 1, in <module>
    var += 5
TypeError: can only concatenate str (not "int") to str
>>> var = int(var)
>>> var += 4
>>> var
14
>>> var = "1.7"
>>> var = int(var)
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    var = int(var)
ValueError: invalid literal for int() with base 10: '1.7'
>>> round(var)
Traceback (most recent call last):
  File "<pyshell#266>", line 1, in <module>
    round(var)
TypeError: type str doesn't define __round__ method
>>> var = -2.8
>>> var = "-2.8"
>>> var = int(var)
Traceback (most recent call last):
  File "<pyshell#269>", line 1, in <module>
    var = int(var)
ValueError: invalid literal for int() with base 10: '-2.8'
>>> var = -2.8
>>> var = int(var)
>>> var
-2
>>>      Hello         world
     
SyntaxError: unexpected indent
>>>    Name     Class
   
SyntaxError: unexpected indent
>>>      Hi        6A
     
SyntaxError: unexpected indent
>>> 	Amy        6F
	
SyntaxError: unexpected indent
>>> print("%7s%10s" % ("Name", "Class"))
   Name     Class
>>> x, y = 2,3
>>> for i in range(3):
	x += 1
	y += 2
	print("%7d%10d" % (x, y))

	
      3         5
      4         7
      5         9
>>> for i in range(3):
	if i == 0:
		print("%7s%10s" % ("Name", "Class"))
	x += 1
	y += 2
	print("%7d%10d" % (x, y))

	
   Name     Class
      6        11
      7        13
      8        15
>>> import math
>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> help(math)
Help on module math:

NAME
    math

MODULE REFERENCE
    https://docs.python.org/3.8/library/math
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.
        
        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.
        
        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    dist(p, q, /)
        Return the Euclidean distance between two points p and q.
        
        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.
        
        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(x, y, /)
        greatest common divisor of x and y
    
    hypot(...)
        hypot(*coordinates) -> value
        
        Multidimensional Euclidean distance from the origin to a point.
        
        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))
        
        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).
        
        For example, the hypotenuse of a 3/4/5 right triangle is:
        
            >>> hypot(3.0, 4.0)
            5.0
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    isqrt(n, /)
        Return the integer part of the square root of the input.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    perm(n, k=None, /)
        Number of ways to choose k items from n items without repetition and with order.
        
        Evaluates to n! / (n - k)! when k <= n and evaluates
        to zero when k > n.
        
        If k is not specified or is None, then k defaults to n
        and the function returns n!.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    prod(iterable, /, *, start=1)
        Calculate the product of all the elements in the input iterable.
        
        The default start value for the product is 1.
        
        When the iterable is empty, return the start value.  This function is
        intended specifically for use with numeric values and may reject
        non-numeric types.
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload/math.cpython-38-darwin.so


>>> print(math.sqrt(5))
2.23606797749979
>>> from math import sqrt
>>> print(sqrt(4))
2.0
>>> print(floor(5))
Traceback (most recent call last):
  File "<pyshell#293>", line 1, in <module>
    print(floor(5))
NameError: name 'floor' is not defined
>>> print(math.floor(4))
4
>>> import numpy
>>> help(numpy)

