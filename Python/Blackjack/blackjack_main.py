# To know basic idea of this game:
# Checkout => https://games.washingtonpost.com/games/blackjack

################ Our Blackjack House Rules ####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###############################################################

import blackjack_art
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Initial amount in both players' acoount
dealer_cash = 1000
player_cash = 1000
player_win = 1

def add_card(total):
    card_provided = random.choice(cards)
    #this condition will decide whether to use 'ACE' card as 1 or 11
    if card_provided == 11:
        if total+card_provided > 21:
            card_provided = 1
    return card_provided

#To print result of each game
def result (a,b,a_cards,b_cards):
    global player_win
    if a>21:
        player_win = 0
        return "You went over. You lose 😭"
    elif b>a and b<=21:
        player_win = 0
        #to check whether dealer got a blackjack
        if b==21 and len(b_cards)==2:
            return "Dealer got a blackjack. You lost 😥"
        return "You lose 😤"
    elif a>b and a<=21:
        player_win = 1
        #to check whether player got a blackjack
        if a==21 and len(a_cards)==2:
            return "You got a blackjack. You win 😄"
        return "You win 🙃"        
    elif b>21 and a<=21:
        player_win = 1
        return "Dealer went over. You win 😀"
    else:
        player_win = -1
        return "It's a draw 😬 "
  
    
if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    game_continue = True
else:
    game_continue = False

while game_continue:
    os.system('clear')
    dealer_cards = []
    player_cards = []
    dealer_total = 0
    player_total = 0
    player_continue = True
    print (blackjack_art.logo)
    print("\nBalance:")
    print(f"    Dealer: {dealer_cash}")
    print(f"    Player: {player_cash}")
    cash_deal = int(input("Make a deal($1, $5, $25, $50, $100, $500, $1000): $"))
    for i in range(2):
        dealer_cards.append(add_card(dealer_total))
        player_cards.append(add_card(player_total))
        dealer_total+=dealer_cards[i]
        player_total+=player_cards[i]
            
    while dealer_total < 16:
        dealer_cards.append(add_card(dealer_total))
        dealer_total+=dealer_cards[len(dealer_cards)-1]
            
    print(f"    Your cards: {player_cards}, current score: {player_total}")
    print(f"    Computer's first card: {dealer_cards[0]}")
           
    while player_total < 21 and player_continue:
        player_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if player_choice == 'y':
            player_cards.append(add_card(player_total   ))
            player_total+=player_cards[len(player_cards)-1]
            print(f"    Your cards: {player_cards}, current score: {player_total}")
        else:
            player_continue = False
    
    print(f"    Your final hand: {player_cards}, final score: {player_total}")
    print(f"    Computer's final hand: {dealer_cards}, final score: {dealer_total}")
    print(result(player_total, dealer_total,player_cards,dealer_cards))
    
    if player_win == 1:
        player_cash += cash_deal
        dealer_cash -= cash_deal
    
    if player_win == 0:
        player_cash -= cash_deal
        dealer_cash += cash_deal
    
    if player_cash <=0 or dealer_cash <=0:
        game_continue = False
        if player_cash <=0:
            print(blackjack_art.you_lost)
        else:
            print(blackjack_art.you_won)         
    else:
        if input("Do you want to play again a game of Blackjack? Type 'y' or 'n': ") == 'y':
            game_continue = True
        else:
            game_continue = False