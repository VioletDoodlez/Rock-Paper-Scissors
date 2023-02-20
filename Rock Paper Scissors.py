import random
import os

os.system("cls")
print("Welcome to Rock, Paper, Scissors, Lizard, Spock: Big Bang Theory Edition!")

userWinningCombinations = (("Scissors", "Paper"), ("Scissors", "Lizard"), ("Rock", "Scissors"), ("Rock", "Lizard"), ("Paper", "Rock"), ("Paper", "Spock"), ("Spock","Rock"), ("Spock", "Scissors"), ("Lizard", "Paper"), ("Lizard","Spock"))
userLosingCombinations = (("Paper", "Scissors"), ("Lizard", "Scissors"), ("Scissors", "Rock"), ("Lizard", "Rock"), ("Rock","Paper"), ("Spock", "Paper"), ("Rock", "Spock"), ("Scissors", "Spock"), ("Paper", "Lizard"), ("Spock", "Lizard"))
winningVerbs = ("cuts", "decapitates", "crushes", "crushes", "covers", "disprouves", "vaporizes", "smashes", "eats", "poisons")
rps = ("Rock", "Paper", "Scissors", "Lizard", "Spock")
validUserInputs = ('r','p','c','l','s','q','cs')

def getValidUserInput():
    userInput = input("Please choose (R)ock, (P)aper, s(C)issors, (L)izard, (S)pock. To quit, press (Q).").lower()

    while not userInput in validUserInputs:
        userInput = input("Oops! Try again! Please choose (R)ock, (P)aper, s(C)issors, (L)izard, (S)pock. To quit, press (Q).").lower()
    return userInput

userInput = getValidUserInput()
while userInput in validUserInputs:
    userIndex = validUserInputs.index(userInput)
    if userIndex == 5:
        break
    if userIndex == 6:
        print("It's simple: Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.")
    else:
        userChoice = rps[userIndex]
        computerChoice = random.choice(rps)
        if userChoice == computerChoice:
            print (f"Tie! We both picked: {computerChoice}.")
        if (userChoice, computerChoice) in userWinningCombinations:
            print (f"User wins! {userChoice} {winningVerbs[userWinningCombinations.index((userChoice, computerChoice))]} {computerChoice}.")
        if (userChoice, computerChoice) in userLosingCombinations:
            print (f"Computer wins! {computerChoice} {winningVerbs[userLosingCombinations.index((userChoice, computerChoice))]} {userChoice}.")
    userInput = getValidUserInput()
    userIndex = validUserInputs.index(userInput)
    if userIndex == 5:
        break
    if userIndex == 6:
        print("It's simple: Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.")

print("See you soon!")