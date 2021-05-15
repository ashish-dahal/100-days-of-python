import random as rd

user_choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
)
inputs = {"0": "Rock", "1": "Paper", "2": "Scissors"}
computer_choice = str(rd.randint(0, 2))

print(f"You choose: {inputs[user_choice]}\n")
print(f"Computer chooses: {inputs[computer_choice]}")

result = user_choice + computer_choice

win = ["02", "10", "21"]
lose = ["20", "01", "12"]

if user_choice == computer_choice:
    print("It is a draw. Try again!\n")
elif result in win:
    print("You win!")
elif result in lose:
    print("You lose!")
