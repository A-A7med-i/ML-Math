import random


def get_heads_probability():
    """
    Simulates flipping a coin and returns 1 for heads, 0 for tails.
    """
    coin_flip = random.choice(["Heads", "Tails"])
    return 1 if coin_flip == "Heads" else 0


heads_count = sum(get_heads_probability() for _ in range(1000))

probability_heads = heads_count / 1000

print(probability_heads)
# 0.489 first output
# 0.517 second output
