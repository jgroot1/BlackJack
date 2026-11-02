from utils.yes_no import *

def player_turn(shuffled_deck, card_values):

    draw_card = True
    hand = []
    hand_value = 0

    while True:

        if draw_card:
        # adds a card to the players hand
            hand += [shuffled_deck.pop(0)]
            hand_value += card_values[hand[-1]]
            print("card drawn")

        # stops the loop if the player does not want a card
        elif draw_card is False:
            print(f"hand: {" ,".join(hand)}\n"
                  f"hand value: {hand_value}\n")
            break

        if len(hand) >= 2:
            # lets the player hit or stand and gives information about the hand if the player has 2 or more cards
            if hand_value <= 21:

                print(f"hand: {" ,".join(hand)}\n"
                      f"hand value: {hand_value}\n")

                draw_card = choice("draw a card?", "drawing card", "standing")

            if hand_value == 21:
                print("Blackjack!")
                draw_card = False

            if hand_value > 21:
                print("bust!")
                draw_card = False
