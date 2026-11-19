from utils.ace_converter import ace_converter

# draws 2 cards for the dealer checks for 21 and shows only the first card
def dealer_begin(shuffled_deck, card_values):

    # gives 2 cards to the dealer
    dealer_hand = shuffled_deck[:2]
    shuffled_deck = shuffled_deck[2:]
    print(f"----------dealer hand ---------")

    # checks for 21
    if card_values[dealer_hand[0]] + card_values[dealer_hand[1]] == 21:
        print("dealer has blackjack\n"
             f"dealer hand: {" and ".join(dealer_hand)}\n")
        dealer_hand = "blackjack"

    # prints the dealers card
    else:
        print(f"dealer hand {dealer_hand[0]}\n"
              f"Dealer hand value {card_values[dealer_hand[0]]}\n")

    return dealer_hand, shuffled_deck

# the turn for the dealer
def dealer_turn(dealer_hand, shuffled_deck, card_values):

    # skips dealer turn if the dealer has blackjack
    if dealer_hand == "blackjack":
        return dealer_hand, shuffled_deck, card_values

    # start dealer turn
    dealer_value = sum(card_values[card] for card in dealer_hand)
    print("----------dealer turn ---------\n"
          f"dealer hand {", ".join(dealer_hand)}\n"
          f"dealer value {dealer_value}")

    while True:
        # dealer draws while total card value of the dealer lower than 16
        if dealer_value <= 16:
            print(f"dealer draws {shuffled_deck[0]}\n")

            dealer_hand += [shuffled_deck.pop(0)]
            dealer_value = sum(card_values[card] for card in dealer_hand)

            print("----------dealer hand ---------\n"
                  f"dealer hand {", ".join(dealer_hand)}\n"
                  f"dealer value {dealer_value}\n")

        # handling hand values higher than 21 with aces
        if dealer_value > 21:
            ace_converter(dealer_hand, card_values)
            dealer_value = sum(card_values[card] for card in dealer_hand)

            if dealer_value > 21:
                print("dealer bust!")
                dealer_hand = "bust"
                return dealer_hand, shuffled_deck, card_values

        elif dealer_value >= 17:
            print("dealer stands on", dealer_value)
            return dealer_hand, shuffled_deck, card_values
