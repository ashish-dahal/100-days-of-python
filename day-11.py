# Blackjack Capstone Project

import random

cards = [
    ("A", 11),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
    ("6", 6),
    ("7", 7),
    ("8", 8),
    ("9", 9),
    ("10", 10),
    ("J", 10),
    ("Q", 10),
    ("K", 10),
]


def choose_cards():
    return random.choice(cards)


def get_cards(hand):
    return [card[0] for card in hand]


def evaluate_winner(player_hand, computer_hand):
    player_score = 0
    computer_score = 0
    for card in player_hand:
        player_score += card[1]
    for card in computer_hand:
        computer_score += card[1]
    print(player_score, computer_score)
    if player_score > 21 or player_score < computer_score:
        return "You lose!"
    elif player_score == computer_score:
        return "It's a tie!"
    return "You win!"


# Draw player and computer hand
player_hand = []
computer_hand = []
for i in range(2):
    player_hand.append(choose_cards())
    computer_hand.append(choose_cards())


# Display Cards
print("Your cards:", get_cards(player_hand))
print("Computer's first card:", get_cards(computer_hand)[0])

# Ask if the player would like to get another card
choice = input("Type 'y' to get another card, type 'n' to pass: ")
if choice == "y":
    player_hand.append(choose_cards())

# Display final hand
print("Your final hand:", get_cards(player_hand))
print("Computer's final hand:", get_cards(computer_hand))

print(evaluate_winner(player_hand, computer_hand))
