def results(player_hand, dealer_hand, card_values):

    print("\n---------- results ----------")
    print(dealer_hand)
    print(player_hand)

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

        print(f"player hand value: {player_value}\n"
              f"dealer hand value: {dealer_value}")

        if dealer_value >= player_value:
            return "dealer wins"
        elif dealer_value <= player_value:
            return "player wins"
        elif dealer_value == player_value:
            return "draw"




"""            if player_hand == "bust":
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
"""