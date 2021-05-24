import random

print(
    "Welcome to the number guessing game.\nI am thinking of a number between 1 and 100."
)

choices = ["easy", "hard"]
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
while 1:
    if difficulty not in choices:
        difficulty = input("Invalid choice. Type 'easy' or 'hard': ")
    else:
        break

if difficulty == "easy":
    attempts_remaining = 10
else:
    attempts_remaining = 5

guess_number = random.randint(1, 100)

while 1:
    print(guess_number)
    print(f"You have {attempts_remaining} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess == guess_number:
        print("Your guess is correct. You win!")
        break
    if user_guess > guess_number:
        print("Too high.")
    else:
        print("Too low.")
    attempts_remaining -= 1
    if attempts_remaining <= 0:
        print(
            f"You couldn't guess the number. The number was {guess_number}. You lose!"
        )
        break
    print("Guess again.")
