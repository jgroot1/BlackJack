def results(player_hand, dealer_hand, card_values):

    print("\n---------- results ----------")
    if type(player_hand) or type(dealer_hand) == str:

        if player_hand == "bust":
            if dealer_hand == "bust":
                print("draw")
                return
            else:
                print("dealer wins")
                return

        elif dealer_hand == "bust":
            print("player wins")
            return

        elif dealer_hand == "blackjack":
            if player_hand == "blackjack":
                print("draw")
                return

            else:
                print("dealer wins")

        elif player_hand == "blackjack":
            print("player wins")
            return

    else:

        dealer_value = sum(card_values[card] for card in dealer_hand)
        player_value = sum(card_values[player] for player in player_hand)

        if dealer_value >= player_value:
            print("dealer wins")
            return
        elif dealer_value <= player_value:
            print("player wins")
            return
        elif dealer_value == player_value:
            print("draw")
            return