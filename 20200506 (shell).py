Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> my mom likes me
Can you explain why your mom likes you?

>> you are not a helpful therapist
Can you explain why you are not a helpful therapist?

>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> you are not a helpful therapist
You seem to think that I are not a helpful therapist?

>> quit
Have a nice day!
>>> history = {}
>>> history[1] = "hello world"
>>> history
{1: 'hello world'}
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> not so good
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 50, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 43, in main
    count += 1
UnboundLocalError: local variable 'count' referenced before assignment
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> not so good
Can you explain why not so good?

>> i couldnt sleep at night
Please continue.

>> i couldnt sleep at night
You seem to think that you couldnt sleep at night?

>> really tired
Please tell me more.

>> I always wake up after 4 hours of sleep only
You seem to think that you always wake up after 4 hours of sleep only?

>> yes
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 50, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 48, in main
    print(reply(sentence))
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 23, in reply
    if probability == 2 and count > 3:
NameError: name 'count' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> I always wake up after 4 hours of sleep only
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 50, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 48, in main
    print(reply(sentence))
TypeError: reply() missing 1 required positional argument: 'count'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> I always wake up after 4 hours of sleep only
Can you explain why you always wake up after 4 hours of sleep only?

>> I always wake up after 4 hours of sleep only
You seem to think that you always wake up after 4 hours of sleep only?

>> I always wake up after 4 hours of sleep only
Why do you say that you always wake up after 4 hours of sleep only?

>> I always wake up after 4 hours of sleep only
Earlier you said that you always wake up after 4 hours of sleep only

>> yes
Please tell me more.

>> yes
You seem to think that yes?

>> yes
You seem to think that yes?

>> yes
Why do you say that yes?

>> nah
Earlier you said that nah

>> history
Many of my patients tell me the same thing.

>> history = {}
Why do you say that history = {}?

>> quit
Have a nice day!
>>> history = {}
>>> history[1] = "hello world"
>>> history[2] = "hsiaoting"
>>> len(history)
2
>>> random.randint(len(history))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    random.randint(len(history))
TypeError: randint() missing 1 required positional argument: 'b'
>>> random.randint(1, len(history))
1
>>> random.randint(1, len(history) + 1)
1
>>> random.randint(1, len(history) + 1)
2
>>> history[2]
'hsiaoting'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> I always wake up after 4 hours of sleep only
You seem to think that you always wake up after 4 hours of sleep only?

>> I always wake up after 4 hours of sleep only
Why do you say that you always wake up after 4 hours of sleep only?

>> I always wake up after 4 hours of sleep only
Can you explain why you always wake up after 4 hours of sleep only?

>> I always wake up after 4 hours of sleep only
You seem to think that you always wake up after 4 hours of sleep only?

>> I always wake up after 4 hours of sleep only
You seem to think that you always wake up after 4 hours of sleep only?

>> I always wake up after 4 hours of sleep only
Many of my patients tell me the same thing.

>> hello
You seem to think that hello?

>> world
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 59, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 57, in main
    print(reply(sentence, count))
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 26, in reply
    return "Earlier you said that " + historyRecord()
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 39, in historyRecord
    random = random.randint(1, len(history))
UnboundLocalError: local variable 'random' referenced before assignment
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> hello
You seem to think that hello?

>> my name
You seem to think that your name?

>> hsiaoting
You seem to think that hsiaoting?

>> cant sleep
You seem to think that cant sleep?

>> 4 hours
Why do you say that 4 hours?

>> play piano
Why do you say that play piano?

>> coding
Earlier you said that play piano

>> yep
You seem to think that yep?

>> world
You seem to think that world?

>> couldnt sleep
Can you explain why couldnt sleep?

>> earlier 
Please continue.

>> sleep earlier
Please tell me more.

>> tell you more
Earlier you said that sleep earlier

>> dictionary
Many of my patients tell me the same thing.

>> history
Can you explain why history?

>> what
Why do you say that what?

>> why
Why do you say that why?

>> how
Can you explain why how?

>> when
Many of my patients tell me the same thing.

>> yes
Why do you say that yes?

>> nop
You seem to think that nop?

>> cant 
Please continue.

>> i can
Why do you say that you can?

>> never give up
Can you explain why never give up?

>> resilience
You seem to think that resilience?

>> rc
Earlier you said that how

>> oh yes
You seem to think that oh yes?

>> yea cause
Earlier you said that never give up

>> yea
Earlier you said that rc

>> yea
You seem to think that yea?

>> quit
Have a nice day!
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> you are not helpful
You seem to think that I are not helpful?

>> you yourself
Why do you say that I yourself?

>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> you dont even
Please tell me more.

>> you dont even know
Please continue.

>> you dont even know
You seem to think that I dont even know?

>> you yourself
You seem to think that I myself?

>> yours
Earlier you said that I dont even know

>> not yours
Can you explain why not mine?

>> i was there
Earlier you said that mine

>> i was there
Many of my patients tell me the same thing.

>> i was there
Please continue.

>> i was there
Can you explain why you were there?

>> he was mine
Earlier you said that mine

>> he was mine
Can you explain why he were yours?

>> this was my only memory of him
Why do you say that this were your only memory of him?

>> quit
Have a nice day!
>>> sentence = "hello my name is hsiao ting"
>>> words = sentence.split()
>>> words
['hello', 'my', 'name', 'is', 'hsiao', 'ting']
>>> for i in range(len(words)):
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> for i in range(len(words)):
	print(i)

	
0
1
2
3
4
5
>>> words[0]
'hello'
>>> words[5]
'ting'
>>> replyWords = []
>>> replyWords += "I am"
>>> replyWords
['I', ' ', 'a', 'm']
>>> replyWords.append("I am")
>>> replyWords
['I', ' ', 'a', 'm', 'I am']
>>> replyWords = []
>>> replyWords.append("I am")
>>> replyWords
['I am']
>>> replyWords.append("hsiaoting")
>>> replyWords.append("hello")
>>> replyWords.append("world")
>>> " ".join(replyWords)
'I am hsiaoting hello world'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> you are not good
Many of my patients tell me the same thing.

>> you are not good
Can you explain why I am I am I am I am I are not good I are not good I are not good?

>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> you are not good
You seem to think that I am are not good?

>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> you are not good
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 66, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 60, in main
    history[count] = changePerson(sentence)
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 39, in changePerson
    next(words)
TypeError: 'list' object is not an iterator
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> you are not good
You seem to think that I am?

>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> you are not good
You seem to think that I am are?

>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> you are not good
Many of my patients tell me the same thing.

>> you are not good
Can you explain why I am are not good?

>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Good morning, I hope you are well today.
What can I do for you?

>> you are not good
Why do you say that I am not good?

>> you are not good
You seem to think that I am not good?

>> quit
Have a nice day!
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Enter a positive integer to find factorial: 2
2
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Enter a positive integer to find factorial: 4
24
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Enter a positive integer: 4
4
3
2
1
None
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Enter a positive integer: 4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 116, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 114, in main
    print(example(n))
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 108, in example
    example(n)
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 108, in example
    example(n)
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 108, in example
    example(n)
  [Previous line repeated 14 more times]
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 107, in example
    print(n)
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Enter a sentence and a number: hello,0
ollehNone
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Enter a sentence and a number: hello world,0
dlrow ollehNone
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Enter a sentence and a number: 
	hello,0
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 116, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200506 (file).py", line 112, in main
    aString, index = n.split(",")
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Enter a sentence and a number: hello,0
ollehNone
>>> aString = "hello"
>>> aString[0]
'h'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Enter a sentence and a number: hello,0
hello
>>> 