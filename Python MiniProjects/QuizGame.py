print("Wecome to my game ")
ans = input("Do you want to play? ")
if ans.lower() == "yes":
    print("let's go ")
else:
    quit()
score = 0
a = input("What does CPU stands for? ").lower()
if a == "centrel processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect! ")
a = input("What does RAM stands for? ").lower()
if a == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect! ")
a = input("What does ROM stands for? ").lower()
if a == "read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect! ")
a = input("What does OOP stands for? ").lower()
if a == "object oriented programming":
    print("Correct!")
    score+=1
else:
    print("Incorrect! ")

print("Thank you for playing the game")
print("You got "+str(score)+" points")
print("The pecentage of correct answers is "+str(score/4*100)+"%")
