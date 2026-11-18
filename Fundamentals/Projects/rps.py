import random

choices = ["rock","paper","scissors"]

computer = random.choice(choices)

player = None
while player not in choices:
    player = input("Rock, paper or scissors? ").lower()

if player == computer:
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    print("It's a tie!")
elif player == "rock":
    if computer == "paper":
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("You lose!")
    if computer == "scissors":
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("You win!")
elif player == "paper":
    if computer == "rock":
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("You win!")
    if computer == "scissors":
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("You lose!")
elif player == "scissors":
    if computer == "rock":
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("You lose!")
    if computer == "paper":
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("You win!")
