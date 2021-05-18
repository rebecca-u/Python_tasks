#this program will ask the user for their name and ask them to think of a random number.

import random #use the import random library to be able to use random numbers

myName = input("Hi! What is your name?") #this is the variable which is for the users name.

number = random.randint(1,10) #variable containing the random number

print("Well, " + myName + " I am thinking of a number between 1 and 10.")
guess = int(input("Can you guess the number I am thinking of?"))#user needs to guess a number and input it.

if guess == number:
    print("Good job, "+ myName + "you are correct.") #if their guess is correct 
else:
    print("oh no! That is the wrong answer, " + myName +" better luck next time!")#if guess is wrong
    
    #at the end the program will show what the correct number was.
print("The computer number was", number)

