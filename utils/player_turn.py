from utils.yes_no import *
from utils.ace_converter import *

def player_turn(shuffled_deck, card_values):

    # draws 2 cards
    hand = shuffled_deck[:2]
    shuffled_deck = shuffled_deck[2:]

    while True:
        # prints hand
        hand_value = sum(card_values[card] for card in hand)
        print("---------- current hand ----------\n"
              f"hand: {" ,".join(hand)} \n"
              f"Hand value: {hand_value} \n")

        if hand_value == 21:
            print("Blackjack!")
            return

        if hand_value > 21:
            ace_converter(hand, card_values)
            hand_value = sum(card_values[card] for card in hand)
            if hand_value > 21:
                print("bust!")
                return

        # choice for drawing card
        if hand_value <= 21:
            draw_card = choice("draw a card?", "drawing card", "standing")

            # draws card
            if draw_card:
                print(shuffled_deck[0],"drawn")
                hand += [shuffled_deck.pop(0)]

            # quits on blackjack, bust and stand
            elif not draw_card:
                print("---------- player final hand ----------\n"
                      f"hand: {" ,".join(hand)}\n"
                      f"hand value: {hand_value}\n")
                return

