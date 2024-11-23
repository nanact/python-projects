
import random as rand

while True:
    Select = ["rock","paper","scissor"]
    
    computer = rand.choice(Select)
    
    Player = input("Enter a choose (rock paper scissor)")
    
    if computer == Player :
        print(f"It is a tie, Computer choice: {computer}, Your choose {Player}")
        
    elif (Player == "paper" and computer == "rock") or (Player == "rock" and computer == "scissor") or (Player == "scissor" and computer == "paper"):
        print(f"you win , Computer choice: {computer}, Your choices: {Player} ")
        
    else:
        print(f"you lose, computer choice: {computer}, Your choices: {Player}")
        
    yesorno = input("Do you want to continue y or n")
    
    if yesorno != "y":
        break
        