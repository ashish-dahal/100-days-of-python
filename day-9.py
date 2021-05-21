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

max_bid = 0
max_index = 0

for bidder in bids:
    if bids[bidder] > max_bid:
        max_bid = bids[bidder]
        max_bidder = bidder

print(f"The winner is {max_bidder} with a bid of {max_bid}.")
