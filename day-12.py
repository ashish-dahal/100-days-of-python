import random


def choose_difficulty():
    choices = ["easy", "hard"]
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    while True:
        if difficulty not in choices:
            difficulty = input("Invalid choice. Type 'easy' or 'hard': ")
        else:
            break
    return 10 if difficulty == "easy" else 5


print(
    "Welcome to the number guessing game.\nI am thinking of a number between 1 and 100."
)

attempts_remaining = choose_difficulty()

guess_number = random.randint(1, 100)

while True:
    print(f"You have {attempts_remaining} attempts remaining to guess the number.")

    user_guess = int(input("Make a guess: "))

    if user_guess == guess_number:
        print("Your guess is correct. You win!")
        break

    print("Too high.") if user_guess > guess_number else print("Too low.")

    attempts_remaining -= 1
    if attempts_remaining <= 0:
        print(f"You've run out of guesses. The number was {guess_number}. You lose!")
        break
    print("Guess again.")
