import random

ans = input("Do you want to play the game? ").lower()
if ans == "yes":
    print("Let's go! ")
else:
    quit()

upperRange = input("Enter an upper bound: ")
if upperRange.isdigit():
    upperRange = int(upperRange)
    if upperRange <= 0:
        print("Enter a positive upper bound next time ")
        quit()
else:
    print("Enter a number next time ")
    quit()
randomNumber = random.randint(0,upperRange)
guesses = 0

while True:
    guesses += 1
    guess = input("Please guess the number ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Enter a number next time: ")
        continue
    if guess == randomNumber:
        print("Your guess is correct")
        break
    elif guess > randomNumber:
        print("Your guess is greater than the number ")
    else:
        print("Your guess is lesser then the number ")
    
print("You got it in",guesses,"guesses") 

            
    
    
    

    

