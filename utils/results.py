def results(player_hand, dealer_hand, card_values):

    print("\n---------- results ----------")

    if (player_hand  in ["bust", "blackjack"] or
         dealer_hand in ["bust", "blackjack"]):


        match player_hand, dealer_hand:

            case "blackjack", "blackjack":
                return "draw"
            case "blackjack", _:
                return "player wins"
            case _, "blackjack":
                return "dealer wins"
            case "bust", _:
                return "dealer wins"
            case _, "bust":
                return "player wins"

    else:

        dealer_value = sum(card_values[card] for card in dealer_hand)
        player_value = sum(card_values[player] for player in player_hand)

        print(f"player hand: {" ,".join(player_hand)}\n"
              f"player hand value: {player_value}\n\n"
              
              f"dealer hand: {" ,".join(dealer_hand)}\n"
              f"dealer hand value: {dealer_value}\n")

        if dealer_value >= player_value:
            return "dealer wins"
        elif dealer_value <= player_value:
            return "player wins"
        elif dealer_value == player_value:
            return "draw"


