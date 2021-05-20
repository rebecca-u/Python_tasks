import random


def intro():
    name = input("Hello. What is your name? ") #ask for user's name and store as a variable.
    print("Hi! " + name + " I'm thinking of a random number between 1 and 100.")

def main():
    global randomNumber
    # Create a random number
    randomNumber = random.randrange(1, 101)

    # Initialize our attempt count, we start with attempt 1.
    user_attempt_number = 1

    # Set user guess to something secret number can't be, so we can
    # get our 'while' loop started.
    user_guess = 0

    # Loop until user_guess is the random number, or we run out of attempts.
    while user_guess != randomNumber and user_attempt_number < 10:
         

        # Tell the user what attempt we are on, and get their guess:
        print("\n--- Attempt", user_attempt_number)
        user_input = input("Guess what number I am thinking of: ")
        user_guess = int(user_input)

        # Print if we are too high or low, or we got it.
        if user_guess > randomNumber:
            print("Too high.")
        elif user_guess < randomNumber:
            print("Too low.")
        else:
            print("You got it!")
           

         # Set user guess to something secret number can't be, so we can
    # get our 'while' loop started.
    user_guess = 0

    # Loop until user_guess our secret number, or we run out of attempts.
    while user_guess != randomNumber and user_attempt_number < 10:

# Call the main function
        intro()
        main()
