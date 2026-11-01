# setup
import random
from utils.yes_no import *

from utils.player_turn import *

deck = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "jack": 10, "queen": 10, "king": 10, "ace": 11}
suits = ["hearts", "diamonds", "clubs", "spades"]

# deck with the card values
card_values = {f"{card} of {suit}": card_value for suit in suits for card, card_value in deck.items()}

# create the deck that is being shuffled and the cards get pulled from
shuffled_deck = random.sample(list(card_values), len(card_values))

# drawing card
player_turn(shuffled_deck, card_values)