import random

deck = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "jack": 10, "queen": 10, "king": 10, "ace": 11}
suits = ["hearts", "diamonds", "clubs", "spades"]

# deck with the card values
full_deck = {f"{card} of {suit}": card_value for suit in suits for card, card_value in deck.items()}

# create the deck that is being shuffled and the cards get pulled from
shuffled_deck = random.sample(list(full_deck), len(full_deck))

# draws cards
play = True
hand = []
while play:
    draw_card = None
    while draw_card is None:
        try:
            draw_card = input("Draw a card? (y/n): ")
            if draw_card in ["y", "yes"]:
                print("Drawing card")
                draw_card = True
            elif draw_card in ["n", "no"]:
                print("Not drawing card")
                draw_card = False
            else:
                raise ValueError
        except ValueError:
            print("Please enter either yes or no.\n")
            draw_card = None