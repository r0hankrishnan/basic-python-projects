#User will pick a number in their head and define an upper range for the computer
#The computer will make a guess and then ask for feedback (high, low, correct)
#The computer will adjust its guesses based on the feedback

#Import random
import random

#Create computer guessing function
def computer_guess(x):
    lower = 0
    upper = x
    feedback = " "

    while feedback != "c":
        guess = random.randint(lower, upper)
        feedback = input(f"Is {guess} correct(c), too high(h), or too low(l)?")
        if feedback == "h":
            upper = guess - 1
        elif feedback == "l":
            lower = guess + 1

    print(f"Let's goooo I got the number {guess} right")


computer_guess(10)


#Notes:
#In while loops, create iterated variable because if it's outside of it it will be reset and computer won't "learn"
#Recall that while loops keep running (everything within while: and nothing before or after) until break is met
#Set ultimate judge criteria before while loop (in this case feedback)