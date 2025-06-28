import random

def classical_computer():
    coin = random.choice([0,1])
    return coin

print(f"Classical Result: {classical_computer()}")
