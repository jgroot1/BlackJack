def blackjack_for_bot():
    # setup for defualt values when bot plays
    epsilon = 0.5
    learn_rate = 0.1,
    rewards = {"player": 1, "draw": -0.5, "dealer": -1}
    discount_factor = 1
    q_table = {}
