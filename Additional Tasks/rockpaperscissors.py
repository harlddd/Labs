import random
import time

def play_round():
    choice = ["rock", "paper", "scissors"]
    computer = random.choice(choice)
    user = input("Enter your choice (rock/paper/scissors): ")
    time.sleep(0.5)
    print(f"Computer chose: {computer}")
    if user.lower() == computer:
        return "tie"
    elif user.lower() == "rock":
        if computer == "scissors":
            return "user"
        else:
            return "computer"
    elif user.lower() == "paper":
        if computer == "rock":
            return "user"
        else:
            return "computer"
    elif user.lower() == "scissors":
        if computer == "paper":
            return "user"
        else:
            return "computer"
    else:
        time.sleep(0.5)
        print("Invalid choice. Please try again.")
        return play_round()

rounds = 0
userwin = 0
computerwin = 0
draw = 0
replay = "y"

while replay.lower() == "y":
    rounds += 1
    result = play_round()
    if result == "user":
        userwin += 1
        time.sleep(0.5)
        print("You win!")
    elif result == "computer":
        computerwin += 1
        time.sleep(0.5)
        print("Computer wins!")
    else:
        draw += 1
        time.sleep(0.5)
        print("Draw.")
    
    time.sleep(0.5)
    print(f"Rounds played: {rounds}")
    time.sleep(0.5)
    print(f"User wins: {userwin}")
    time.sleep(0.5)
    print(f"Computer wins: {computerwin}")
    time.sleep(0.5)
    print(f"Draws: {draw}")
    time.sleep(0.5)
    replay = input("Would you like to play again? (y/n) ")
    time.sleep(0.5)