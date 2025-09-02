# Number Guessing Game

import random

def guessing_game():
    number=random.randint(1,100)
    attempts=0

    while True:
        guess=int(input("guess a number between 1 and 100"))
        attempts+=1

        if(guess>number):
            print("guess lower")
        elif(guess<number):
            print("guess higher")
        elif guess==number:
            print("you got it right in" + attempts + "attempts")
            break

guessing_game()