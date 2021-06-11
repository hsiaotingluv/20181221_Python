# press <cmd> <shift> <U>, terminal, type <python> to run python, can use calculator 

#how to change input to integer
#Add int BEFORE input to change to integer
number = int(input("Enter number: "))
solution = number + 1

print (solution)



#how to input
#always remember to add variable
x = input("Enter name: ")
print ("Hey " + x)
input("Press <Enter>") #make sure the file stays there until you want to close it



#printing ""
"bucky said, \"hey now\" to me"
#when using  as an EL language, put (\) in front to tell python to ignore



#Adding a string
a = "hey "
b = "hsiaoting"
a + b = "hey hsiaoting"



#printing a str and number
num = 18
print ("hsiaoting is " + num)
#ERROR! you cant add a letter to a number!
#change the num from integer to string!
num = str(18)
print ("hsiaoting is " + num)
#Add str BEFORE input to change to string
num = str(input("Enter a number: "))
print ("you are " + num)



#list, []
# counting from the front: first index 0, second index 1 and so on
family = ['mom','dad','dog','sis']
family[3] = 'sis'
#counting from the back: last index = -1, second last = -2 and so on
family[-4] = 'mom'
#string can also be a list
"hsiaoting"[3] = 'a'



#slicing [ : ]
#include first index, exclude last index
family = ['mom','dad','dog','sis']
family[1:3] = ['dad', 'dog'] #include only index 1,2 exclude 3
#to include rest of all number, leave empty
family[-4:] = ['mom', 'dad', 'dog', 'sis'] #or
family[:] = ['mom', 'dad', 'dog', 'sis']
#reverse list
family[::-1] = ['sis', 'dog', 'dad', 'mom']
#when you use negative, it always start from the last index, then increment from there on
letters = ['a','b','c','d','e','f','g']
letters[::-3] = ['g', 'd', 'a']

