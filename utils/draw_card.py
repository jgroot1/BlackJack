# function to draw a card to a hand
def draw(amount, hand, shuffled_deck):

    for _ in range(amount):
        hand.append(shuffled_deck.pop(0))

    return hand, shuffled_deck