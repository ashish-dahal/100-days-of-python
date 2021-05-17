# Hangman game

# setup utilities
import os
from random import randint

logo = """
  _   _                                         
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 |  _  | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    |___/                       

"""

stages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
]

words = (
    "ant baboon badger bat bear beaver camel cat clam cobra cougar "
    "coyote crow deer dog donkey duck eagle ferret fox frog goat "
    "goose hawk lion lizard llama mole monkey moose mouse mule newt "
    "otter owl panda parrot pigeon python rabbit ram rat raven "
    "rhino salmon seal shark sheep skunk sloth snake spider "
    "stork swan tiger toad trout turkey turtle weasel whale wolf "
    "wombat zebra "
).split()

# Start the program
print(logo)

# Choose a random word from the word list
word_to_guess = words[randint(0, len(words) - 1)]
guessed = ["_" for letter in word_to_guess]

# Initialize utility variables
lives = len(stages)
stages = stages[::-1]
remaining_letters = word_to_guess

# Check the guess
while lives != 0:
    # Initialize message prompt to the user
    prompt = ""

    # Take a guess from the user
    guess = input("Guess a word:\n")
    os.system("cls")

    # If guess is correct
    if guess in remaining_letters:
        remaining_letters = remaining_letters.replace(guess, "")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                guessed[i] = guess
        prompt = f"You guessed {guess}, that's in the word."
    elif remaining_letters == "":
        prompt = "You guessed the word. You win."
        break
    # If guess is incorrect
    else:
        prompt = f"You guessed {guess}, that's not in the blanks. You lose a life."
        lives -= 1

    # Display the outcome
    print(" ".join(guessed) + "\n")
    print(prompt + "\n")
    print(stages[lives - 1] + "\n")

    # End the game if all lives lost
    if lives == 0:
        os.system("cls")
        print(stages[0] + "\n")
        print("Your hangman died. You lose.")
        break
