#program which will ask the user for 2 numbers and offer them options of 4 maths operators to choose. 
# the calculation is performed by using a procedure and passing parameters. 

#print welcome message and brief explanation of program.
print("Welcome to my Python calculator.\nI can help you to perform addition, subtraction, multiplication and division calculations.")
## This is my procedure that passes 3 values. 
def calc(sign, num1, num2): #this is the procedure passing parameters
    if sign == "a":
        maths = num1 + num2 #if statement for adding
        print("The answer to your mathematical calculation is:", maths)
    elif sign  == "b":
        maths = num1 - num2 #elif statement for subtracting
        print("The answer to your mathematical calculation is: ", maths) 
    elif sign == ("c"):
        maths = num1 * num2#elif statement for multiplying
        print("The answer to your mathematical calculation is: ", maths)
    elif sign == "d":
        maths =num1 / num2#elif statement for dividing
        print("The answer to your mathematical calculation is: ", maths)
    else:
        print("Wrong operator")#error message if option is not offered in menu.
        
#This is the main code
num1 = int(input("Enter the first number: "))#user required to input first number 

num2 = int(input("Enter the second number: "))#user required to input second number  
#user is offered menu of operator calculation options to choose.
print ("Select a - if you want to add.\nSelect b - if you want to subtract.\nSelect c - if you want to multiply.\nSelect d - if you want to divide.")
#user must select and enter the operator 
sign = input("Enter either a, b, c or d to perform the required calculation: ")

calc(sign, num1, num2)#procedure is called to be performed