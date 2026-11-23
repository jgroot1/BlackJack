import random

from utils.choice import choice
from utils.dealer import dealer_start, dealer_turn
from utils.player_turn import player_turn
from utils.results import results


def main():
    # setup
    deck = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
            "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
    suits = ["hearts", "diamonds", "clubs", "spades"]
    wins = {"player": 0, "dealer": 0, "draw": 0}

    # game loop
    play = True
    while play:
        # deck with the card values
        card_values = {f"{card} of {suit}": card_value for suit in suits for card, card_value in deck.items()}

        # create the deck that is being shuffled and the cards get pulled from
        shuffled_deck = random.sample(list(card_values), len(card_values))

        # dealer draws 2 checks for 21 and shows 1 card
        dealer_hand, shuffled_deck = dealer_start(shuffled_deck, card_values)

        # drawing card
        player_hand, shuffled_deck, card_values = player_turn(shuffled_deck, card_values, dealer_hand)

        # dealers turn
        dealer_hand, shuffled_deck, card_values = dealer_turn(dealer_hand, shuffled_deck, card_values, player_hand)

        # outputs a winner, the winner value is not in use
        winner = results(player_hand, dealer_hand, card_values, wins)

        # lets the user play again
        play = choice("play again",
                      "restarting\n\n--------------- new game ---------------\n",
                      "exiting")


if __name__ == "__main__":
    main()
