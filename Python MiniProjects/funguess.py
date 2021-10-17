import random
# Human guessing the number generated by computer
def fun(x):
    random_number = random.randint(1,x)
    guess = 0
    count = 0
    while(guess != random_number):
        guess = int(input("Enter your guess: "))
        if(guess<random_number):
            print("Sorry, your guess is too low")
            count+=1
        else:
            print("Sorry, your guess is too high")
            count+=1
    print(f"Hurray, you got the number {random_number} in {count} guesses")

n = int(input("Enter the upper range: "))
fun(n)
# Computer guessing the number that the user knows
def comp(n):
    feedback =""
    low = 1
    high = n
    
    while feedback!= "c":
        if(low!=high):
            num = random.randint(low,high)
        else:
            num = low
        feedback = input(f"Is {num} to low (l) or too High (h), or is it correct ").lower()
        if(feedback=="l"):
            low = num+1
        elif(feedback=="h"):
            high = num-1
    print(f'Hurray!, The computer guessed your {num} correctly')   





n = int(input("Enter the upper range: "))
comp(n)



    