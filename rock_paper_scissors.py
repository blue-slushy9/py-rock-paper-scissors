# Play rock-paper-scissors against the computer!

# Hint: involves the random module

import random

print("This is Rock-Paper-Scissors! You will be playing against the computer. Please enter your selection now...")
human = input().lower()

objects = ["rock","paper","scissors"]

computer = random.choice(objects).lower()

print(f"You chose {human}, and the computer chooses {computer}.")
print()

if human == "rock" and computer == "paper":
    print("Paper covers rock, therefore you lose!")

elif human == "rock" and computer == "scissors":
    print("Rock breaks scissors, therefore you win!")

elif human == "paper" and computer == "scissors":
    print("Scissors cut paper, therefore you lose!")

elif human == "paper" and computer == "rock":
    print("Paper covers rock, therefore you win!")

elif human == "scissors" and computer == "rock":
    print("Rock breaks scissors, therefore you lose!")

elif human == "scissors" and computer == "paper":
    print("Scissors cut paper, therefore you win!")

else:
    print("Both you and the computer chose the same object, therefore it's a stalemate.")