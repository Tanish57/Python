import os

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#HINT: You can call clear() to clear the output in the console.
from blindauctionart import logo
print(logo)
flag = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #bidding_record = {"Tanish" : 123, "Sarthak" : 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of {highest_bid}")



bids = {}
while(flag):
  name = input("Enter Your name: ")
  bid_price = int(input("Enter your bid: $"))
  
  bids[name] = bid_price

  if input("Other bidders? type yes or no : ") == "yes":
    clear()
  else:
    flag = False

find_highest_bidder(bids)