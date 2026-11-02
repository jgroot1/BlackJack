# setup
import random
from utils.dealer import *
from utils.player_turn import *

deck = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
suits = ["hearts", "diamonds", "clubs", "spades"]

# deck with the card values
card_values = {f"{card} of {suit}": card_value for suit in suits for card, card_value in deck.items()}

# create the deck that is being shuffled and the cards get pulled from
shuffled_deck = random.sample(list(card_values), len(card_values))
shuffled_deck = ["Ace of hearts", "Ace of spades", "Ace of diamonds", "Ace of clubs", "Two of Hearts", "Two of Spades", "Two of Diamonds", "Two of Clubs"]
print(shuffled_deck)

# dealer draws 2 checks for 21 and shows 1 card
dealer_hand, shuffled_deck = dealer_begin(shuffled_deck, card_values)

# drawing card
player_turn(shuffled_deck, card_values)

#dealers turn
dealer_turn(dealer_hand, shuffled_deck, card_values)