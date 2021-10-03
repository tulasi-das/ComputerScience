name = input("Enter your name: ")
answer = input("Do you want to play: ").lower()
if answer == 'yes':
    print("Let's go",name)
else:
    quit()
answer = input('You reached to junction which side do you want to go left or right? ').lower()
if answer == 'right':
    answer = input("You reached to a river, you want swim across or walk over ").lower()
    if answer == 'swim':
        print("You swam across the river and eaten by an alligator ")
    elif answer =='walk':
        print("You walked for miles and ran out of water, you lost ")
    else:
        print("Not a valid option, You lose")
elif answer == 'left':
    answer = input("You reached a bridge, it looks wobbly, you wanna cross it or go back(cross/goback)").lower()
    if answer == "cross":
        print("You met a person, and he gave you gold, You Won!")
    elif answer == 'goback':
        print("You went back, you lost")
    else:
        print("You didn't entered a valid input you lost")
else:
    print("Not a valid option, you lose")
print("Thank you for playing the game", name)
