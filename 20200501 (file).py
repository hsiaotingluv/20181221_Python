#Chapter 5
#sentence generator
'''
import random

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def sentence():
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()
'''

#Mode of a list of values
'''
fileName = input("Enter the filename: ")
f = open(fileName, "r")

words = []
for line in f:
    for word in line.split():
        words.append(word.upper())

theDictionary = {}
for word in words:
    number = theDictionary.get(word, None)
    if number == None:
        theDictionary[word] = 1
    else:
        theDictionary[word] = number + 1

theMaximum = max(theDictionary.values())

for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print("The mode is", key)
        break

f.close()
'''

#Case Study
#Nonedirective Psychotherapy
'''
import random

hedges = ("Please tell me more.", \
          "Many of my patients tell me the same thing.", \
          "Please continue.")

replacements = {"i":"you", "my":"your", "me":"you", \
                "we":"you", "us":"you", "mine":"yours"}

qualifiers = ("Why do you say that", \
              "You seem to think that", \
            "Can you explain why")

def reply(sentence):
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + " " + changePerson(sentence) + "?"

def changePerson(sentence):
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
        #if key is in dictionary, print out the changed word
        #if key not in dictionary, print out the original word
    return " ".join(replyWords)
        #change a list of words into a sentence with spacings

#or using mapping
def changePerson(sentence):
    def getWord(word):
        return replacements.get(word, word)
    return " ".join(map(getWord, sentence.split())
                    
def main():
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        sentence = sentence.lower()
        if sentence == "quit":
            print("Have a nice day!")
            break
        print(reply(sentence))

# The entry point for program execution
main()
'''
        
