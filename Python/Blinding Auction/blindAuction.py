# This program is designed so that we can organize blind auction at a small platform


import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bid_details = {}
bid_continue = True
max_bid = 0
winner = ""

print(logo)
print("Welcome to the secret auction program.")

while bid_continue:
    name = input("What is your name?: ")
    bid_price = float(input("What's your bid?: $"))
    bid_details[name] = bid_price
    if bid_price > max_bid:
        max_bid = bid_price
        winner = name
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if continue_bid == 'yes':
        os.system('clear')
    else:
        bid_continue = False
        print(f"Hence, the highest bid is ${max_bid} made by {winner}.")
    