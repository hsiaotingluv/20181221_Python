#Chapter 5 Projects
#9, 10
'''
import random

hedges = ("Please tell me more.", \
          "Many of my patients tell me the same thing.", \
          "Please continue.")

replacements = {"i":"you", "my":"your", "me":"you", \
                "we":"you", "us":"you", "mine":"yours", \
                "you":"I","am":"are", "myself":"yourself", \
                "yourself":"myself", "was":"were", \
                "your":"my", "yours":"mine"}

qualifiers = ("Why do you say that", \
              "You seem to think that", \
              "Can you explain why")

history = {}

def reply(sentence, count):
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    if probability == 2 and count > 3:
        return "Earlier you said that " + historyRecord()
    else:
        return random.choice(qualifiers) + " " + changePerson(sentence) + "?"

def changePerson(sentence):
    words = sentence.split()
    replyWords = []
    i = 0
    it = iter(words)
    
    for word in it:
        if words[i] == "you" and words[i + 1] == "are":
            replyWords.append("I am")
            next(it)
            #skip the next loop
        else:
            replyWords.append(replacements.get(word, word))
        i += 1

    return " ".join(replyWords)

def historyRecord():
    number = random.randint(1, len(history))

    return history[number]
    
def main():
    count = 0
    
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        sentence = sentence.lower()
        count += 1
        history[count] = changePerson(sentence)
        if sentence == "quit":
            print("Have a nice day!")
            break
        print(reply(sentence, count))

main()
'''

#Chapter 6 Design with Functions                
#Exercises
#2
'''
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

def main():
    n = int(input("Enter a positive integer to find factorial: "))
    print(fact(n))

main()
'''

#4
#prints "4 /n 3 /n 2 /n 1 /n None"
'''
def example(n):
   if n > 0:
        print(n)
        example(n - 1)
    #print none when stops

def main():
    n = int(input("Enter a positive integer: "))
    print(example(n))

main()    
'''

#6
#prints "ollehNone"
'''
def example(aString, index):
   if index < len(aString):
       example(aString, index + 1)
       #call recursive function before printing -> reverse order
       print(aString[index], end = "")
     

def main():
    n = input("Enter a sentence and a number: ")
    aString, index = n.split(",")
    index = int(index)
    print(example(aString, index))

main()
'''

#7
#prints "hello"
'''
def example(aString, index):
    if index == len(aString):
       return ""
    else:
       return aString[index] + example(aString, index + 1)

def main():
    n = input("Enter a sentence and a number: ")
    aString, index = n.split(",")
    index = int(index)
    print(example(aString, index))

main()
'''

