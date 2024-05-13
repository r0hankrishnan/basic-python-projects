#Create a function that allows user to play a game of RPS against computer using "random"

#Psuedocode
#User inputs a choice of R, P, S
#Computer randomly generates a choice of R, P, S
#If statemetn to check all combinations to see who wins

#Import random
import random

#Create rock, paper, scissors function
def rock_paper_scissors():
    play_again = " "

    while play_again != "n":
        user_choice = input("Pick rock(r), paper(p), or scissors(s): ").strip()
        com_choice = random.choice(["r", "p", "s"])

        if user_choice == "r" and com_choice == "r":
            print(f"User choice: {user_choice}")
            print(f"Computer choice: {com_choice}")
            print("It's a tie!")
            play_again = input("Play again? (y/n): ")

        elif user_choice == "r" and com_choice == "p":
            print(f"User choice: {user_choice}")
            print(f"Computer choice: {com_choice}")
            print("Computer wins!")
            play_again = input("Play again? (y/n): ")

        elif user_choice == "r" and com_choice == "s":
            print(f"User choice: {user_choice}")
            print(f"Computer choice: {com_choice}")
            print("User wins!")
            play_again = input("Play again? (y/n): ")

        elif user_choice == "p" and com_choice == "r":
            print(f"User choice: {user_choice}")
            print(f"Computer choice: {com_choice}")
            print("User wins!")
            play_again = input("Play again? (y/n): ")

        elif user_choice == "p" and com_choice == "p":
            print(f"User choice: {user_choice}")
            print(f"Computer choice: {com_choice}")
            print("It's a tie!")
            play_again = input("Play again? (y/n): ")

        elif user_choice == "p" and com_choice == "s":
            print(f"User choice: {user_choice}")
            print(f"Computer choice: {com_choice}")
            print("Computer wins!")
            play_again = input("Play again? (y/n): ")

        elif user_choice == "s" and com_choice == "r":
            print(f"User choice: {user_choice}")
            print(f"Computer choice: {com_choice}")
            print("Computer wins!")
            play_again = input("Play again? (y/n): ")

        elif user_choice == "s" and com_choice == "p":
            print(f"User choice: {user_choice}")
            print(f"Computer choice: {com_choice}")
            print("User wins!")
            play_again = input("Play again? (y/n): ")

        elif user_choice == "s" and com_choice == "s":
            print(f"User choice: {user_choice}")
            print(f"Computer choice: {com_choice}")
            print("It's a tie!")
            play_again = input("Play again? (y/n): ")

    print("Thanks for playing!")

rock_paper_scissors()