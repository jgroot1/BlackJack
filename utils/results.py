# function for giving the resuelts of the blackjack game
def results(player_hand, dealer_hand, card_values, wins):
    print("\n---------- results ----------\n")

    if (player_hand in ["bust", "blackjack"] or
        dealer_hand in ["bust", "blackjack"]):

        # used for when the player or dealer has blackjack or is bust
        match player_hand, dealer_hand:
            case "blackjack", "blackjack":
                winner = "draw"
            case "blackjack", _:
                winner = "player"
            case _, "blackjack":
                winner = "dealer"
            case "bust", _:
                winner = "dealer"
            case _, "bust":
                winner = "player"

    else:
        # used when the player and dealer both have a hand of cards instead of blackjack or bust
        player_value = sum(card_values[player] for player in player_hand)
        dealer_value = sum(card_values[card] for card in dealer_hand)

        # print the players and the dealers hand
        print(" ---player hand---\n"
              f"{" ,".join(player_hand)}\n"
              f"Hand value: {player_value}\n\n"
              " ---dealer hand---\n"
              f"{" ,".join(dealer_hand)}\n"
              f"Hand value: {dealer_value}\n")

        # outputs who has won
        if player_value >= player_value:
            winner = "player"
        elif player_value <= player_value:
            winner = "dealer"
        elif player_value == player_value:
            winner = "draw"

    # prints who has won
    if winner in ["dealer", "player"]:
        print(winner, "has won!\n")
    else:
        print("Draw!\n")

    # prints and counts the amount each person has won
    wins[winner] += 1
    print(
        f"You have won {wins["player"]} times\n"
        f"dealer has won {wins["dealer"]} times\n"
        f"there were {wins["draw"]} draws\n")

    return winner
