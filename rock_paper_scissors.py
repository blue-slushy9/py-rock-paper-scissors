# Play rock-paper-scissors against the computer!

# The random.choice() method allows you to pick an element at random, in this
# case from a list;
from random import choice

# Throughout this program, I use many print() statements to enhance legibility
# in the terminal, e.g. below;
print()
print("This is Rock-Paper-Scissors! You will be playing against the computer. Please enter your selection now...")
print()

# We use lower() to control for human error in the input, e.g. "ROCK";
human = input().lower()
print()

objects = ["rock","paper","scissors"]

computer = choice(objects).lower()

print(f"You chose {human}, and the computer chooses {computer}.")
print()

if human in objects:

    if human == "rock" and computer == "paper":
        print("Paper covers rock, therefore you lose!")
        print()

    elif human == "rock" and computer == "scissors":
        print("Rock breaks scissors, therefore you win!")
        print()

    elif human == "paper" and computer == "scissors":
        print("Scissors cut paper, therefore you lose!")
        print()

    elif human == "paper" and computer == "rock":
        print("Paper covers rock, therefore you win!")
        print()

    elif human == "scissors" and computer == "rock":
        print("Rock breaks scissors, therefore you lose!")
        print()

    elif human == "scissors" and computer == "paper":
        print("Scissors cut paper, therefore you win!")
        print()

    else:
        print("Both you and the computer chose the same object, therefore it's a stalemate.")
        print()

else:
    print("This is an invalid input, please run the program again from the\n"
            "beginning.")
    print()
