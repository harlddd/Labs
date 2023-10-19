import random

class rps:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.userscore = 0
        self.computerscore = 0
        self.draw = 0
        self.rounds = 0

    def play_game(self):
        while True:
            userchoice = input("\033[34mChoose rock, paper or scissors: \033[0m")
            computerchoice = random.choice(self.choices)

            print(f"\033[34mPlayer choice: {userchoice}\033[0m")
            print(f"\033[34mComputer choice: {computerchoice}\033[0m")

            if userchoice not in self.choices:
                print("\033[33mInvalid choice. Try again.\033[0m")
            elif userchoice == computerchoice:
                print("\033[0;36mRound Draw!\033[0m")
                self.draw +=1
            elif (userchoice == 'rock' and computerchoice == 'scissors'):
                print("\033[0;36mYou win!\033[0m")
                self.userscore += 1
            elif (userchoice == 'paper' and computerchoice == 'rock'):
                print("\033[0;36mYou win!\033[0m")
                self.userscore += 1
            elif (userchoice == 'scissors' and computerchoice == 'paper'):
                print("\033[0;36mYou win!\033[0m")
                self.userscore += 1
            else:
                print("\033[0,36mThe computer wins!\033[0m")
                self.computerscore += 1

            self.rounds += 1

            print(f"\033[34mRounds played: {self.rounds}\033[0m")
            print(f"\033[34mPlayer score: {self.userscore}\033[0m")
            print(f"\033[34mComputer score: {self.computerscore}\033[0m")
            print(f"\033[34mRounds Drawn: {self.draw}\033[0m\n")

            play_again = input("\033[31;5mDo you want to play again? (y/n) \033[0m")
            if play_again.lower() == 'y':
                continue
            else:                
                print("\033[33mThanks for playing!\033[0m")
                break

play = rps()
play.play_game()