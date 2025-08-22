#ASSIGNMENT 1
import random
x=random.randint(1,100)
guess=int(input("Guess a number between 1 and 100.\n Enter the number:"))
attempts=1
while guess!=x:
    if guess>x:
        print("Too high")
        guess=int(input("Guess a number between 1 and 100.\n Enter the number"))
    elif guess<x:
        print("Too low")
        guess=int(input("Guess a number between 1 and 100.\n Enter the number:"))
    attempts+=2
else:
    print("you guessed right!!!")
    print(f"you guessed {attempts}times")