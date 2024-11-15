# prog_dictionary = {
#     "Banana": "Yellow",
#     "Apple": "Red",
#     "Berry": "Blue",
# }
#
# print(prog_dictionary["Banana"])
#
# for i in prog_dictionary:
#     print(i, prog_dictionary[i])

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]
#
# print(nested_list[2][0])
#
# travel_log = {
#     "France": {
#             "total_visits": 5,
#             "cities_visited": ["Paris", "Dijon", "Lille"]
#     },
#     "Germany": {
#         "cities_visited": ["Stuttgart", "Berlin"],
#         "total_visits": 3
#
#     }
# }
#
# print(travel_log["Germany"]["cities_visited"][0])

import os

print("Welcome to the secret auction program!\n")

# Create an empty dictionary to store names and bids
bids = {}

# Loop to keep asking for new entries
while True:
    # Get user input for name and bid
    name = input("What is your name?:\n")
    bid = int(input("What is your bid?:\n"))

    # Add the name and bid to the dictionary
    bids[name] = bid

    # Clear the screen
    print("\n"*100)

    # Ask if the user wants to add another entry
    should_continue = input("Are there any other bidders? Type 'yes' to continue or 'no' to stop:\n").lower()
    if should_continue != 'yes':
        break

# Find the highest bid and declare the winner
highest_bid = 0
winner = ""

for bidder, amount in bids.items():
    if amount > highest_bid:
        highest_bid = amount
        winner = bidder

print(f"\nThe winner is {winner} with a bid of ${highest_bid}!")





