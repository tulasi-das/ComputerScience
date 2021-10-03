import random

userWins = 0
computerWins = 0
options = ["rock","paper","scissors"]
while True:
    userInput = input("Enter Rock/Paper/Scissors or Q to quit ").lower()
    if userInput == 'q':
        break
    if userInput not in options:
        print("Enter a valid input ")
        continue
    random = random.randint(0,2)
    # 0 ->Rock, 1 -> Paper, 2-> Scissors
    computerPick = options[random]
    print("Computer picked",computerPick+".")
    if userInput == 'rock' and computerPick == 'scissors':
        print("You won! ")
        userWins+=1
    elif userInput == 'paper' and computerPick == 'rock':
        print("You won! ")
        userWins+=1
    elif userInput == 'scissors' and computerPick == 'paper':
        print("You won! ")
        userWins+=1
    else:
        print("Computer won! ")
        computerWins+=1
    
print("You won",userWins,"times")
print("Computer won",computerWins,"times")
print("Good bye!")