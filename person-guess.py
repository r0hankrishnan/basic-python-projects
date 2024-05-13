#Computer will generate a random number between 1 and an inputted value x
#Person will input guesses and get feedback on whether it is too high or too low until they guess correctly

#Import random package
import random

#Create guess game as a function
def guess(x):
    number = random.randint(1,x)
    guess = 0
    while guess != number:
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if guess > number:
            print("Your guess was too high!")
        elif guess < number:
            print("Your guess was too low!")
    
    print(f"Congrats, you guessed the number {guess} correctly!")

guess(10)