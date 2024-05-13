# Remake the rock, paper, scissors game without having to explicitly define each potential outcome
#Instead of listing each case, you can just define the tie and win scenarios and the rest have to be losses

#Import random
import random

#Create game
def better_rps():
    play_again = " "
    user_choice = " "

    while play_again != "n":
        user_choice = input("Pick rock(r), paper(p), or scissors(s): ").strip()
        com_choice = random.choice(["r", "p", "s"])

        if user_choice == com_choice:
            print("It's a tie!")
            play_again = input("Would you like to play again? (y/n) ")
            
        
        #If statements are boolean so don't need to explicitly define "true" after statement
        if win(user_choice, com_choice) == True:
            print(f"Your choice: {user_choice}")
            print(f"Computer choice: {com_choice}")
            print(f"You win!")
            play_again = input("Would you like to play again? (y/n) ")
            
        
        #Lose scenario (runs if win() returns false)
        print(f"Your choice: {user_choice}")
        print(f"Computer choice: {com_choice}")
        print(f"You lose!")
        play_again = input("Would you like to play again? (y/n) ")
    
    #Runs after player says they don't want to play again
    print("Thanks for playing!")

#Define win function
def win(user, com):
    if (user == "r" and com == "s") or (user == "p" and com == "r") or (user == "s" and com == "p"):
        return True
    
    return False

better_rps()