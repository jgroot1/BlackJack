from utils.yes_no import *

def player_turn(shuffled_deck, card_values):

    draw_card = True
    hand = []
    hand_value = 0

    while True:

        if draw_card is True:

        # adds a  card to the players hand
            hand += [shuffled_deck.pop(0)]
            hand_value += card_values[hand[-1]]

        # stops the loop if the player does not want a card
        elif draw_card is False:
            turn = False
            print(f"hand value {hand_value}\n"
                  f"hand {hand}\n")
            return

        # lets the player hit or stand and gives information about the hand if the player has 2 or more cards
        if len(hand) >= 2:

            print(f"hand value {hand_value}\n"
                  f"hand {hand}")

            draw_card = choice("draw a card?", "drawing card", "standing")


