import os
from auction_logo import logo
print(logo)
print("Welcome to my auction bidding program.")
def find_highest_bidder(bidding_record):

    highest_bid = 0
    winner = ""
    for bid in bids:
        bid_price = bids[bid]
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bid
    print(f"{winner} offered the highest bid of {highest_bid}. He is the winner!")

bids = {}
next_person = True
while next_person:
    bidder_name = input("Please enter your name: ").upper()
    bid_amount = int(input("How much do you offer as your paying price? #"))
    bids[bidder_name]  = bid_amount
    more_bids = input("Do you have more bids? Type 'yes' or 'no' :").lower()
    more_bids_answer = False
    while not more_bids_answer:
        if more_bids == "no":
            next_person = False
            more_bids_answer = True
        elif more_bids == "yes":
            more_bids_answer = True
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            answer = input("I do not understand your inputs. Please enter 'yes' or 'no' from the keyboard. \n")
            more_bids = answer
greatest_bidder = print(find_highest_bidder(bids))