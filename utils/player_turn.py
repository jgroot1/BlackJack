from utils.choice import choice
from utils.ace_converter import ace_converter

def player_turn(shuffled_deck, card_values,dealer_hand):

    # draws 2 cards
    player_hand = shuffled_deck[:2]
    shuffled_deck = shuffled_deck[2:]
    player_value = sum(card_values[card] for card in player_hand)

    # stops player turn on blackjack
    if player_value == 21:
        player_hand = "blackjack"
        print("--- Blackjack!---\n")
        return player_hand, shuffled_deck, card_values

    # stops player turn when the dealer has blackjack
    if dealer_hand == "blackjack":
        return player_hand, shuffled_deck, card_values

    while True:

        # prints hand
        player_value = sum(card_values[card] for card in player_hand)
        print("---------- current hand ----------\n"
              f"hand: {" ,".join(player_hand)}\n"
              f"Hand value: {player_value}\n")

        # ends the player turn if the hand is above 21 and there is not an ace that can be converted into a 1
        if player_value > 21:
            ace_converter(player_hand, card_values)
            player_value = sum(card_values[card] for card in player_hand)

            if player_value > 21:
                player_hand = "bust"
                print("---bust!---\n")
                return player_hand, shuffled_deck, card_values

        # choice for drawing card
        if player_value <= 21:
            draw_card = choice("draw a card?", "drawing card\n", "standing\n")

            # draws card
            if draw_card:
                print(shuffled_deck[0],"drawn\n")
                player_hand += [shuffled_deck.pop(0)]

            # quits on blackjack, bust and stand
            if not draw_card:
                print("---------- player final hand ----------\n"
                        f"hand: {" ,".join(player_hand)}\n"
                        f"hand value: {player_value}\n")
                return player_hand, shuffled_deck, card_values
