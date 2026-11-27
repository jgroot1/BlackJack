import random

#Q(S,A) = Q(S,A) + α * (R + γ Q(S′,A′) − Q(S,A))

#state = (player_value, dealer_value, usable_ace)

# chooses an action
# state -> player_hand_value, dealer_value, usable_ace
# action = choose_action(state, epsilon)
def choose_action(state, epsilon, q_table4):

    if random.random() < epsilon:
        epsilon *= 0.9995 if epsilon > 0.01 else 0.01
        print(epsilon)
        print("random action")
        return random.choice(["hit", "stand"])

    return max(["hit", "stand"], key=lambda action: q_table.get((state, action), 0))




player_value = sum(card_values[player] for player in player_hand)
            dealer_value = sum(card_values[card] for card in dealer_hand)
            for ace in ["Ace of hearts", "Ace of spades", "Ace of diamonds", "Ace of clubs"]:
                if ace in player_hand and card_values[ace] == 11:
                    usable_ace = True
                else:
                    usable_ace = False
            state = (player_value, dealer_value, usable_ace)


learn_rate = 0.1,
rewards  = {"player": 1, "draw": -0.5, "dealer": -1}[winner]
discount_factor = 1


state = (player_value, dealer_hand, usable_ace)


def Q_learn(state, winner):


    Q(state, action) = Q(state, action) + learn_rate * (reward + discount_factor * Q(state, action) - Q(state, action))

    return Q(state, action)

