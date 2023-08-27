# This function allows Python to generate random numbers
import random

# Cheeky welcome into the game
print("Welcome to Efe's Game of Pig! ")

"""
Function to roll the dice here
A number with a value between 1 and 6 will be returned
When this function is called
"""
def roll_dice():
    return random.randint(1, 6)

"""
This function sets up the actions for the player's turn
Their score will start at 0
The player has the choice to roll the die or hold
When rolling, they will get a number between 1 and 6
The value of this roll will be displayed on the screen
This will continue until they hold or roll a 1
If they roll a 1, their score will return to 0
If they hold, their score will be saved and displayed on the screen
If the user does not roll or hold, they will be asked to try again
"""
def player_turn():
    turn_score = 0
    while True:
        choice = input("Roll or Hold? (r/h): ")
        if choice == "r":
            roll = roll_dice()
            print(f"You rolled a {roll}")
            if roll == 1:
                print("You rolled a 1. Your turn is over.")
                return 0
            else:
                turn_score += roll
                print(f"Your current score for this turn: {turn_score}")
        elif choice == "h":
            return turn_score
        else:
            print("Invalid choice. Try again.")
"""
This is a similar function to the player's turn, but the computer rolls automatically
It does not have the ability to hold
If the computer gets 20 or more in a turn, the game will switch back to the player's turn
"""
def computer_turn():
    turn_score = 0
    while True:
        roll = roll_dice()
        print(f"The computer rolled a {roll}")
        if roll == 1:
            print("The computer rolled a 1. Its turn is over.")
            return 0
        else:
            turn_score += roll
            print(f"The computer's current score for this turn: {turn_score}")
            if turn_score >= 20:
                return turn_score
"""
This is the function to play the game
Both the player and the computer start with a score of 0
While both the player and the computer have a score of less than 100, the game continues
If the player reaches a score of 100 or more, the while loop will be exited
If the player reaches a score of 100 or more, a congratulatory message is printed
The number of turns used to win is printed as well
If the computer wins, the number of turns it took for it to win will be printed
"""
def play_game():
    player_score = 0
    computer_score = 0
    turns = 0
    while player_score < 100 and computer_score < 100:
        print("=== Player's Turn ===")
        player_score += player_turn()
        turns += 1
        print(f"Your score: {player_score}\n")

        if player_score >= 100:
            break

        print("=== Computer's Turn ===")
        computer_score += computer_turn()
        turns += 1
        print(f"Computer score: {computer_score}\n")
    
    if player_score >= 100:
        print(f"Congratulations! You won in {turns} turns.")
    else:
        print(f"The computer won in {turns} turns.")

# Function is called to begin the game
play_game()
