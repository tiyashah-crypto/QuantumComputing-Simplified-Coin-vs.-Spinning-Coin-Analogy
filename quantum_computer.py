import random

def quantum_computer():
    coin = "0+1"
    return coin if random().random() < 0.5 else coin

print(f"Quantum Result : {quantum_computer()}")
