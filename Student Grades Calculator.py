def mark_grade():#use procedure to change percentage mark to grade
    mark = int(input("what is your % mark : "))#asks user their percentage mark and stores it in a variable called mark.
    
    #if statement that outputs different strings depending on the percentage mark
    #stored in the mark variable.
    if mark < 0 or mark > 100:#error message if mark entered is less than 0 or more than 100.
        print("You need to input number between 0 and 100 only! Try again!")
    elif 90 <= mark <= 100:
        mark_result = "A*"
        print("Amazing, you got an A*!!!")
    elif 80 <= mark< 90:
        mark_result = "A"
        print("Well done, you got an A!!!")
    elif 70 <= mark < 80:
        mark_result = "B"
        print("Good job, you got a B!")
    elif 60 <= mark < 70:
        mark_result = "C"
        print("You got C!")
    else:
        mark_result = "F"
        print("You got F.")
    
    target = input("What is your target grade?: ")#asks user for target and stores in variable
     #if statements that output different strings after comparing the target variable and the mark_result.
    if target.upper() == mark_result: #.upper() function is used to return any lowercase grades entered into uppercase characters.
        print("You acheived your target!")
    elif target.upper() >= mark_result:
        print("Well done! you achieved HIGHER than your target grade.")
    elif target.upper() <= mark_result:
        print("Bad luck. You didn't achieve your target grade.")
    else:
        print("Bad luck. You didn't achieve your target grade.")

mark_grade()#procedure is called to run.
 