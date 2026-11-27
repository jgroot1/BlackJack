import random
from utils.choice import choice

def one_time_setup():
    bot_plays = choice("use bot? (n to play yourself)",
                       "training bot",
                       "starting game")
    deck = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
            "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
    suits = ["hearts", "diamonds", "clubs", "spades"]
    wins  = {"player": 0, "dealer": 0, "draw": 0}

    return bot_plays, deck, suits, wins

def game_reset_setup(deck, suits):
    # deck with the card values
    card_values = {f"{card} of {suit}": card_value for suit in suits for card, card_value in deck.items()}

    # create the deck that is being shuffled and the cards get pulled from
    shuffled_deck = random.sample(list(card_values), len(card_values))

    return card_values, shuffled_deck