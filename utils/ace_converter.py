# converts the value of aces from 11 to 1 if the hand value is higher than 21
def ace_converter(hand,card_values):
    # looks for aces in the hand
    for ace in ["Ace of hearts", "Ace of spades", "Ace of diamonds", "Ace of clubs"]:

        # replaces the aces in the hand when the hand value higher is than 21
        hand_value = sum(card_values[card] for card in hand)
        if ace in hand and card_values[ace] == 11 and hand_value > 21:
            card_values[ace] = 1
            print(f"{ace}, now has a value of one")

        elif hand_value <= 21:
            return hand, card_values