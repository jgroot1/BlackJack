# draws 2 cards for the dealer checks for 21 and shows only the first card
def dealer_begin(shuffled_deck, card_values):

    # gives 2 cards to the dealer
    dealer_hand = shuffled_deck[:2]
    shuffled_deck = shuffled_deck[2:]
    print("dealer hand", dealer_hand[0])
    print(f"Dealer hand value {card_values[dealer_hand[0]]} \n")

    # checks for 21
    if card_values[dealer_hand[0]] + card_values[dealer_hand[1]] == 21:
        print("dealer wins")
        print(f"dealer_hand: {" and ".join(dealer_hand)}\n")

    return dealer_hand, shuffled_deck

# the turn for the dealer
def dealer_turn(dealer_hand, shuffled_deck, card_values):
    dealer_draws_cards = True

    while dealer_draws_cards:

        dealer_value = sum(card_values[card] for card in dealer_hand)
        print(f"dealer hand {dealer_hand}\n"
              f"dealer value {dealer_value}")

        # dealer draws while total card value of the dealer lower than 16
        if dealer_value <= 16:
            dealer_hand += [shuffled_deck.pop(0)]

        # handeling hand values higher than 21 with aces, also needs to be in the player
        elif dealer_value > 21:

            for ace in ["Ace of hearts", "Ace of spades", "Ace of diamonds", "Ace of clubs"]:
                if ace in dealer_hand and card_values[ace] == 11:
                    card_values[ace] = 1
                    print(f"{ace}, now has a value of one")
                    dealer_value = sum(card_values[card] for card in dealer_hand)

                    if dealer_value <= 21:
                        print(f"dealer hand {dealer_hand}\n")
                        break

            if dealer_value > 21:
                print(f"dealer bust", dealer_value)
            break

        elif dealer_value >= 17:
            dealer_draws_cards = False
