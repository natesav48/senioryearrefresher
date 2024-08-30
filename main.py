#need error handeling
#produce random num 1-1000
#user guess until number is found
import random
import random


def randomgamething():
    mystery_number = random.randint(1, 1000)
    guessed_correctly = False

    print("random number game")
    print("Guess a number between 1 and 1000")

    while not guessed_correctly:
        try:
            guess = int(input("What do you think the number is?"))

            if guess < mystery_number:
                print("Higher")
            elif guess > mystery_number:
                print("Lower")
            elif guess == mystery_number:
                print("winner winner chicken dinner")
                guessed_correctly = True
        except ValueError:
            print("Invalid input")

randomgamething()

