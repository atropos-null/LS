"""
Problem: The goal of Twenty-One is to try to get as close to 21 as possible without going over. 
If you go over 21, it's a bust, and you lose.
    - input: strings 'stay' or 'hit'
    - output: "Dealer Wins" or "Player Wins"

Data Structure: Dictionary

Algorithm:

    - Initialize deck
    - Deal cards to player and dealer
    - Player turn: hit or stay
        - repeat until bust or stay
        - If player bust, dealer wins.
    - Dealer turn: hit or stay
        - repeat until total >= 17
        - If dealer busts, player wins.
    - Compare cards and declare winner.

"""

import random
import sys


playing_cards = [
        ['Ace of Hearts', 11],
        ['Two of Hearts', 2],
        ['Three of Hearts', 3],
        ['Four of Hearts', 4],
        ['Five of Hearts', 5],
        ['Six of Hearts', 6],
        ['Seven of Hearts', 7],
        ['Eight of Hearts', 8],
        ['Nine of Hearts', 9],
        ['Ten of Hearts', 10],
        ['Jack of Hearts', 10],
        ['Queen of Hearts', 10],
        ['King of Hearts', 10],
        ['Ace of Diamonds', 11],
        ['Two of Diamonds', 2],
        ['Three of Diamonds', 3],
        ['Four of Diamonds', 4],
        ['Five of Diamonds', 5],
        ['Six of Diamonds', 6],
        ['Seven of Diamonds', 7],
        ['Eight of Diamonds', 8],
        ['Nine of Diamonds', 9],
        ['Ten of Diamonds', 10],
        ['Jack of Diamonds', 10],
        ['Queen of Diamonds', 10],
        ['King of Diamonds', 10],
        ['Ace of Clubs', 11],
        ['Two of Clubs', 2],
        ['Three of Clubs', 3],
        ['Four of Clubs', 4],
        ['Five of Clubs', 5],
        ['Six of Clubs', 6],
        ['Seven of Clubs', 7],
        ['Eight of Clubs', 8],
        ['Nine of Clubs', 9],
        ['Ten of Clubs', 10],
        ['Jack of Clubs', 10],
        ['Queen of Clubs', 10],
        ['King of Clubs', 10],
        ['Ace of Spades', 11],
        ['Two of Spades', 2],
        ['Three of Spades', 3],
        ['Four of Spades', 4],
        ['Five of Spades', 5],
        ['Six of Spades', 6],
        ['Seven of Spades', 7],
        ['Eight of Spades', 8],
        ['Nine of Spades', 9],
        ['Ten of Spades', 10],
        ['Jack of Spades', 10],
        ['Queen of Spades', 10],
        ['King of Spades', 10]
    ]

def total(hand):
    """ Determines the score and handles the Ace"""
    sum_val = 0
    aces = 0
    for card in hand:
        name, value = card  # card[0] is the name, card[1] is the value
        sum_val += value
        if "Ace" in name:
            aces += 1
    # correct for Aces
    while sum_val > 21 and aces:
        sum_val -= 10
        aces -= 1
    return sum_val

def player_turn(player_cards, dealer_cards, deck):
    """ To determine the player's hand"""

    while True:
        player_count = total(player_cards)
        print(f"Dealer has {dealer_cards[0][0]} and an unknown card.")
        print(f"You have: {", ".join(card[0] for card in player_hand)}. Your count is {player_count}")
        if player_count > 21:
            print("Bust! Dealer Wins!")
            sys.exit()
        answer = input("You may 'hit' or 'stay': ").lower()
        if answer == 'hit':
            card = deck.pop()
            player_hand.append(card)
        elif answer == 'stay':
            return player_count
        else:
            print("Invalid input. Please type 'hit' or 'stay'.")

def dealer_turn(dealer_cards, deck):
    """ To determine the dealer's hand"""

    while True:
        dealer_count = total(dealer_cards)
        print(f"Dealer has {dealer_cards[0][0]} and an unknown card.")
        if dealer_count < 17:
            card = deck.pop()
            dealer_hand.append(card)
        else:
            return dealer_count

def compare_cards(player_count, dealer_count):

    """ To compare scores and declare the winner. """

    if player_count > dealer_count and player_count <= 21:
        print(f"Player score is {player_count}, Dealer score is {dealer_count}")
        print("Player Wins!")
    elif dealer_count > player_count and dealer_count <= 21:
        print(f"Dealer score is {dealer_count}, Player score is {player_count}")
        print("Dealer Wins!")
    elif dealer_count > 21:
        print(f"Dealer score is {dealer_count}, Player score is {player_count}")
        print("Player Wins!")
    elif player_count > 21:
        print(f"Player score is {player_count}, Dealer score is {dealer_count}")
        print("Player Wins!")
    else:
        print(f"Player score is {player_count}, Dealer score is {dealer_count}")
        print("It's a tie!")

random.shuffle(playing_cards)
stack = playing_cards.copy()

dealer_hand = [stack.pop(), stack.pop()]
player_hand = [stack.pop(), stack.pop()]

player_score = player_turn(player_hand, dealer_hand, stack)
dealer_score = dealer_turn(dealer_hand, stack)
compare_cards(player_score, dealer_score)
