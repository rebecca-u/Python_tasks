#this program will ask for 2 numbers from the user
#then they must decide which calculation they would like to perform and then give the answer.

#greet the user and tell them to think of 2 numbers.
print("Hi. You will be asked to think of 2 numbers and enter them.")
#Ask for 2 numbers from user
number1 = int(input("Enter first number: ")) #ask user to input their first number.
number2 = int(input("Enter second number: "))#ask user to input their second number.
add = number1 + number2 
subtract = number1 - number2
multiply = number1*number2
divide = number1/number2
powerof= pow(number1, number2) #use pow function to find the power of values.

         
print("Now you must select the operation you would like to perform.")
#user needs to choose an operation from the list of operations.
a = print("a. Add")
b = print("b. Subtract")
c = print("c. Multiply")
d = print("d. Divide")
e = print("e. The power of ")
#operations include addition, subtraction, multiplication, division and indices.


while True:
    #Take input from the user to determine which operation they would like to perform.
    choice = input("Enter choice(a/b/c/d/e): ")
    
    #if user chooses to add numbers 
    if choice == "a" :
        print(number1, "+", number2, "=", add)
    
    #if user chooses to subtract numbers 
    elif choice == "b" :
        print(number1, "-", number2, "=", subtract)
        
        #if user chooses to mulitply numbers 
    elif choice == "c" :
        print(number1, "*", number2, "=", multiply)
        
        #if user chooses to divide numbers 
    elif choice == "d" :
        print(number1, "/", number2, "=", divide)
        
        #if user chooses to find the power of the chosen numbers
    elif choice == "e" :
        print(number1, "**", number2, "=", powerof)
       
        #if user's choice is not listed then an error message will be produced.
    else: 
        print("INVALID INPUT!") 
        
        
        
        
        
    
        
        
    
    
    
    
    
    
    
    
        
        
        
        
        
        
    