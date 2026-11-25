import random

#Q(S,A) = Q(S,A) + α * (R + γ Q(S′,A′) − Q(S,A))

q_table = {}

def Q_learn(winner):

    learn_rate = 0.1
    rewards = {"player": 1, "draw": -0.5,  "dealer": -1}
    reward = rewards[winner]
    discount_factor = 1

    Q(State, action) = Q(State, action) + learn_rate * (reward + discount_factor * Q(State, action) - Q(State, action))

    return Q(State, action)


epsilon = 0.5

if random.random() < epsilon:
    epsilon *= 0.9995
    action = random.choice["hit", "stand"]
else:
    Q_learn(winner)
