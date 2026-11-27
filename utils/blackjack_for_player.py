import random

from utils.choice import choice
from utils.game_functions.dealer import dealer_start, dealer_turn
from utils.game_functions.player_turn import setup_player_turn, player_card_drawing
from utils.game_functions.results import results


def black_jack_for_players(deck, suits):
    # game loop
    play = True
    while play:

        # dealer draws 2 checks for 21 and shows 1 card
        dealer_hand, shuffled_deck = dealer_start(shuffled_deck, card_values)

        # setup for the players turn
        player_hand, shuffled_deck, card_values, start_player_turn = setup_player_turn(shuffled_deck, card_values, dealer_hand)

        # starts the player turn if the player gets a turn (will not get a turn on (dealer)blackjack)
        if start_player_turn:
            player_hand, shuffled_deck, card_values = player_card_drawing(player_hand, shuffled_deck, card_values)

        # dealers turn
        dealer_hand, shuffled_deck, card_values = dealer_turn(dealer_hand, shuffled_deck, card_values, player_hand)

        # outputs a winner, the winner value is not in use
        winner = results(player_hand, dealer_hand, card_values, wins)

        # lets the user play again
        play = choice("play again",
                      "restarting\n\n--------------- new game ---------------\n",
                      "exiting")


if __name__ == "__main__":
    black_jack_for_players()
