import random
import os
import re

# Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

# Prompt user to start game or quit
userChoice = input("Start game [s], quit [q]: ").lower()

# Game loop
while userChoice != 'q':
    print("\nRock, Paper, Scissors - Shoot!")

    # Prompt the user to choose R, P, or S
    userChoice = input("Choose your weapon [R]ock, [P]aper, or [S]cissors: ").upper()

    if not re.match("[RPS]", userChoice):
        print("Please choose a valid option: [R]ock, [S]cissors, or [P]aper.")
        continue

    # Echo the user's choice
    print(f"You chose: {userChoice}")

    # Computer's random choice
    choices = ['R', 'P', 'S']
    opponentChoice = random.choice(choices)

    print(f"I chose: {opponentChoice}")

    # Compare choices
    if opponentChoice == userChoice:
        print("Tie!")

    elif opponentChoice == 'R' and userChoice == 'S':
        print("Rock beats scissors, I win!")

    elif opponentChoice == 'S' and userChoice == 'P':
        print("Scissors beats paper, I win!")

    elif opponentChoice == 'P' and userChoice == 'R':
        print("Paper beats rock, I win!")

    else:
        print("You win!")

    # Prompt the user to play again or quit
    userChoice = input("\nPlay again [s], quit [q]: ").lower()

print("Game over.")

