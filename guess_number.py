
import random as rand 

playing = True

print("A number guessing game")

number = str(rand.randint(1, 10))

while playing:

    guess = input("Guess the number (from 1 to 10)")

    if guess == number:
        print("You are correct")
        print("the number was: ",number)

        break

    else:
        print("It is not correct")
