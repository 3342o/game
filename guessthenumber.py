from game import Your_guess
import random
random_number=random.randint(1,100)
win = False
turns = 0
while win==False:
    Your_guess=int(input("Enter a number"))
    turns +=1
    if Your_guess==random_number:
        print("Yay!!! You won")
        print("No. of turns taken are:", turns)
        win == True
        break
    else:
        if Your_guess>random_number:
            print("You guessed a bigger number. Please insert a smaller number")
        else:
            print("You guessed a smaller number. Please insert a greater number")
