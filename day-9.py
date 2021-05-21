# Auction program to display the highest bidder

import os

bids = {}
have_more_bidders = "yes"
print("Welcome to the secret auction program.")
while have_more_bidders == "yes":
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : "))
    bids.update({name: bid})
    have_more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    os.system("cls")

print(
    f"The winner is {max(bids, key=bids.get)} with a bid of {max(list(bids.values()))}."
)
